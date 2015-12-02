
var svgGUI = ( function() {

    /* SVG element styles */
    var svgStyles = ' \
    <style> \
        .svg-btn:hover {cursor: pointer;} \
        * { \
            cursor:default; \
            -webkit-user-select: none; \
            -khtml-user-select: none; \
            -moz-user-select: -moz-none; \
            -o-user-select: none; \
            user-select: none; \
        } \
    </style> \
    ';

    var buttonClassName = "svg-btn";

    return {
    
        'init' : function(svgId) {
            /* Get the first SVG element in specified container */
            var thisSvgObj = document.getElementById(svgId).contentDocument.getElementsByTagName('svg')[0];

            if (thisSvgObj) {
            thisSvgObj.innerHTML = svgStyles + thisSvgObj.innerHTML;
            }

            return {
            // Add event to specified element 
            'attachEvent' : function(ev, id, cb_fn){
                var elm = thisSvgObj.getElementById(id);
                if (elm !== null ) {
                elm.addEventListener(ev, cb_fn, false);
                elm.classList.add(buttonClassName);
                return elm;
                } else {
                return false;
                }
            },

            // Remve event from specified element
            'removeEvent' : function(ev, id, cb_fn){
                var elm = thisSvgObj.getElementById(id);
                if (elm !== null ) {
                elm.removeEventListener(ev, cb_fn, false);
                elm.classList.remove(buttonClassName);
                return elm;
                } else {
                return false;
                }
            }
            }
        }
    }
})()