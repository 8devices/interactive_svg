(function(py8Dev, undefined) {

    var buttonClassName = "cursor-pointer";

    /* SVG element styles */
    var svgStyles = '<style>.ev-click:hover,.ev-mousedown:hover,.ev-mouseup:hover,.ev-dblclick:hover {cursor:pointer;} * {cursor:default;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:-moz-none;-o-user-select:none;user-select:none;}</style>';


    py8Dev.initSVG = function(svgId) {
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
    }

    // Adds event to element 
    py8Dev.eventAdd = function(elm, ev, cb_fn) {
        if (elm !== null ) {
            elm.addEventListener(ev, cb_fn, false);
            elm.classList.add("ev-"+ev);
        }
    }

    // Removes event from element
    py8Dev.eventRemove = function(elm, ev, cb_fn) {
        if (elm !== null ) {
            elm.removeEventListener(ev, cb_fn, false);
            elm.classList.remove("ev-"+ev);
        }
    }

    // Sets element style
    py8Dev.styleSet = function (elmId, propertyObject) {
        if (elmId !== null) {
            for (var property in propertyObject)
                elmId.style[property] = propertyObject[property];
        }
    }

    // Adds new class(-es) to element
    classAdd = function (elmId, classes) {
        if (elmId !== null) {
            if (typeof classes === 'string')
                classes = [classes];

            for (var i = 0; i < classes.length; i++)
                elmId.classList.add(classes[i]);
        }
    }

    // Removes class(-es) from element
    classRemove = function (elmId, classes) {
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
    }

    // Sets element attributes
    py8Dev.attributeSet = function (elmId, attributeObject, remove) {
        remove = remove || false;

        if (elmId !== null) {

            for (var attribute in attributeObject) {
                if (remove) {
                    if (attribute == "class")
                        classRemove(elmId, attributeObject[attribute]);
                    else
                        elmId.removeAttribute(attribute);
                } else {
                    if (attribute == "class")
                        classAdd(elmId, attributeObject[attribute]);
                    else
                        elmId.setAttribute(attribute, attributeObject[attribute]);
                }
            }
        }
    }

}( window.py8Dev = window.py8Dev || {} ))