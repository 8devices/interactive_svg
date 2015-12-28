(function(py8Dev) {

    var options = {
        wsURL : 'ws://localhost:7777/ws',
        debug : false
    };

    // Add styles to SVG element
    var svgStyles = '<style>.ev-click:hover,.ev-mousedown:hover,.ev-mouseup:hover,.ev-dblclick:hover {cursor:pointer;} * {cursor:default;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:-moz-none;-o-user-select:none;user-select:none;}</style>';

    // Store SVG elements in array
    var svgObjects = [];

    // WebSocket object
    var ws = {};
    var wsConnected = false;

    // Initialize library
    py8Dev.init = function(settings){

        options.wsURL = settings.wsURL || options.wsURL;
        options.debug = settings.debug || options.debug;

        // Connect to WebSocket
        wsConnect(options.wsURL);
    };

    // Connect to WebSocket
    var wsConnect = function(wsURL) {

        ws = new WebSocket(wsURL);

        // WS open
        ws.onopen = wsOpen;

        // WS message received
        ws.onmessage = wsReceive;

        // WS closed
        ws.onclose = wsClose;

        // WS error
        ws.onerror = wsError;
    };

    var wsOpen = function(){
        wsConnected = true;

        if (options.debug)
            console.log("WebSocket connected!");
    };

    var wsClose = function(ev){
        wsConnected = false;

        if (options.debug)
            console.log("WebSocket disconnected! (" + ev.code + ")");
    };

    var wsError = function(){
        if (options.debug)
            console.log("WebSocket error!");
    };

    // WebSocked receive
    var wsReceive = function(ev) {
        if (options.debug)
            console.log("WS recv <-| " + ev.data);

        var json = JSON.parse(ev.data);

        var rootNode = document;

        // If need to manipulate element on SVG object initialize it
        if ('svgId' in json) {
            var svgId = json['svgId'];
            if (svgObjects[svgId] === undefined ) {
                svgObjects[svgId] = initSVG(svgId);
            }

            rootNode = svgObjects[svgId];
        }

        if ('elmId' in json) {
            elmObj = rootNode.getElementById(json['elmId']);

            if ('eventRem' in json)
                eventRemove(elmObj, json['eventRem'], wsSendEvent);

            if ('eventAdd' in json)
                eventAdd(elmObj, json['eventAdd'], wsSendEvent);

            if ('attrRem' in json)
                attributeSet(elmObj, json['attrRem'], true);

            if ('attrSet' in json)
                attributeSet(elmObj, json['attrSet']);

            if ('classRem' in json)
                classRemove(elmObj, json['classRem'], true);

            if ('classAdd' in json)
                classAdd(elmObj, json['classAdd']);

            if ('style' in json)
                styleSet(elmObj, json['style']);
        }
    };

    // WebSocked send
    var wsSend = function(msg) {
        ws.send(msg);

        if (options.debug)
            console.log("WS send |-> " + msg);
    }

    // Send events to WS
    var wsSendEvent = function (ev) {
        wsSend('{"' + ev.type + '": "'+ this.id +'"}\r\n');
    };

    // Initialize SVG object
    var initSVG = function(svgId) {
        /* Get the first SVG element in specified container */
        var svgObj = document.getElementById(svgId);
        var svgElm;

        if (svgObj) {
            svgElm = svgObj.contentDocument.getElementsByTagName('svg')[0];
            if (svgElm) {
                // Add additional styles to SVG image
                svgElm.innerHTML = svgStyles + svgElm.innerHTML;
            } else {
                return null;
            }
        } else {
            return null;
        }

        return svgElm;
    };

    /* Adds event(-s) to an element
     * For event naming use event type: https://en.wikipedia.org/wiki/DOM_events
     * eventAdd(elementId, eventType, callBackFunction)
     */
    var eventAdd = function(elm, ev, cb_fn) {
        if (elm !== null ) {

            // If we have string make it as array
            if (typeof ev === 'string')
                ev = [ev];

            // Attach all event listeners to element
            for (var i = 0; i < ev.length; i++) {
                elm.addEventListener(ev[i], cb_fn, false);
                elm.classList.add("ev-"+ev[i]);
            }
        }
    };

    /* Removes event from element
     * eventRemove(elementId, eventType, callBackFunction)
     */
    var eventRemove = function(elm, ev, cb_fn) {
        if (elm !== null ) {

            // If we have string make it as array
            if (typeof ev === 'string')
                ev = [ev];

            // Attach all event listeners to element
            for (var i = 0; i < ev.length; i++) {
                elm.removeEventListener(ev[i], cb_fn, false);
                elm.classList.remove("ev-"+ev[i]);
            }
        }
    };

    // Sets element style
    var styleSet = function (elmId, propertyObject) {
        if (elmId !== null) {
            for (var property in propertyObject)
                elmId.style[property] = propertyObject[property];
        }
    };

    // Adds new class(-es) to element
    var classAdd = function (elmId, classes) {
        if (elmId !== null) {
            if (typeof classes === 'string')
                classes = [classes];

            for (var i = 0; i < classes.length; i++)
                elmId.classList.add(classes[i]);
        }
    };

    // Removes class(-es) from element
    var classRemove = function (elmId, classes) {
        if (elmId !== null) {
            if (classes) {
                if (typeof classes === 'string')
                    classes = [classes];

                for (var i = 0; i < classes.length; i++)
                    elmId.classList.remove(classes[i]);
            } else {
                elmId.removeAttribute("class");
            }
        }
    };

    // Sets or removes (if remove=true) element attributes
    var attributeSet = function (elmId, attributeObject, remove) {
        remove = remove || false;

        if (elmId !== null) {

            // If we got simple string
            if (typeof attributeObject === 'string')
                attributeObject = [attributeObject];

            // If we got array with attribute names
            var isObjArray = (Object.prototype.toString.call(attributeObject) == "[object Array]");

            for (var attribute in attributeObject) {
                if (remove) {

                    // If we have simple array then use value instead of key
                    if (isObjArray)
                        attribute = attributeObject[attribute];

                    // Remove attribute
                    elmId.removeAttribute(attribute);
                } else {
                    // Set attribute
                    elmId.setAttribute(attribute, attributeObject[attribute]);
                }
            }
        }
    };

}( window.py8Dev = window.py8Dev || {} ));