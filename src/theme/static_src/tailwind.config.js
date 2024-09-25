/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                bg_white: "#FAFAFD",
                bg_gray: "#EAEBF9",
                primary_lightest: "#D5D7F2",
                primary_black: "#121670",
                primary_light: "#8D92F2",
                primary_medium: "#636AF2",
                primary_dark: "#3D46F2",
            },
            fontFamily: {
                plus_jakarta_sans: ['Plus Jakarta Sans', 'sans-serif'],        
            },
            animation: {
                'wiggle': 'wiggle 0.5s ease-in-out infinite', // Añade una animación llamada "wiggle"
              },
              keyframes: {
                wiggle: {
                  '0%, 100%': { transform: 'translateX(0px)' }, // Posición inicial y final
                  '50%': { transform: 'translateX(5px)' }, // Movimiento hacia la derecha
                },
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],

    
}
