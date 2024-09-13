(function ($) {
    "use strict"


    /* 1. Proloder */
    $(window).on('load', function () {
        $('#preloader-active').fadeOut(0);
        $('body').css({
            'overflow': 'visible'
        });
    });

    /* 2. sticky And Scroll UP */
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 400) {
            $(".header-sticky").removeClass("sticky-bar");
            $('#back-top').fadeOut(500);
        } else {
            $(".header-sticky").addClass("sticky-bar");
            $('#back-top').fadeIn(500);
        }
    });

    // Scroll Up
    $('#back-top a').on("click", function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });


    /* 3. slick Nav */
// mobile_menu
    var menu = $('ul#navigation');
    if (menu.length) {
        menu.slicknav({
            prependTo: ".mobile_menu",
            closedSymbol: '+',
            openedSymbol: '-'
        });
    }
    ;


    /* 4. MainSlider-1 */

    // h1-hero-active
    function mainSlider() {
        var BasicSlider = $('.slider-active');
        BasicSlider.on('init', function (e, slick) {
            var $firstAnimatingElements = $('.single-slider:first-child').find('[data-animation]');
            doAnimations($firstAnimatingElements);

        });
        BasicSlider.on('beforeChange', function (e, slick, currentSlide, nextSlide) {
            var $animatingElements = $('.single-slider[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
            doAnimations($animatingElements);

        });

        BasicSlider.slick({
            autoplay: true,
            autoplaySpeed: 4000,
            dots: false,
            fade: true,
            arrows: false,
            prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
            nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
            responsive: [{
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                }
            },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        arrows: false
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        arrows: false
                    }
                }
            ]
        });

        function doAnimations(elements) {
            var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            elements.each(function () {
                var $this = $(this);
                var $animationDelay = $this.data('delay');
                var $animationType = 'animated ' + $this.data('animation');
                $this.css({
                    'animation-delay': $animationDelay,
                    '-webkit-animation-delay': $animationDelay
                });
                $this.addClass($animationType).one(animationEndEvents, function () {
                    $this.removeClass($animationType);
                });
            });
        }
    }

    mainSlider();


    /* 4. Testimonial Active*/
    var testimonial = $('.h1-testimonial-active');
    if (testimonial.length) {
        testimonial.slick({
            dots: true,
            infinite: true,
            speed: 1000,
            autoplay: true,
            loop: true,
            arrows: true,
            prevArrow: '<button type="button" class="slick-prev"><i class="ti-arrow-top-left"></i></button>',
            nextArrow: '<button type="button" class="slick-next"><i class="ti-arrow-top-right"></i></button>',
            slidesToShow: 1,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        infinite: true,
                        dots: true,
                        arrow: true
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        arrow: true
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        arrow: true
                    }
                }
            ]
        });
    }


// Single Img slder
    $('.top-job-slider').slick({
        dots: false,
        infinite: true,
        autoplay: true,
        speed: 400,
        centerPadding: '60px',
        centerMode: true,
        focusOnSelect: true,
        arrows: false,
        prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
        nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1400,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    centerMode: false
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    centerMode: false
                }
            },
        ]
    });


// Single Img slder
    $('.team-active').slick({
        dots: false,
        infinite: true,
        autoplay: true,
        speed: 400,
        arrows: true,
        prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
        nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false
                }
            },
        ]
    });


// courses-area
    $('.courses-actives').slick({
        dots: false,
        infinite: true,
        autoplay: true,
        speed: 400,
        arrows: true,
        prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
        nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false
                }
            },
        ]
    });


    // Brand Active
    $('.brand-active').slick({
        dots: false,
        infinite: true,
        autoplay: true,
        speed: 400,
        arrows: false,
        slidesToShow: 5,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },

            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });


    /* 6. Nice Selectorp  */
    var nice_Select = $('select');
    if (nice_Select.length) {
        nice_Select.niceSelect();
    }

    /* 7. data-background */
    $("[data-background]").each(function () {
        $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
    });


    /* 10. WOW active */
    new WOW().init();

// 11. ---- Mailchimp js --------//
    function mailChimp() {
        $('#mc_embed_signup').find('form').ajaxChimp();
    }

    mailChimp();


// 12 Pop Up Img
    var popUp = $('.single_gallery_part, .img-pop-up');
    if (popUp.length) {
        popUp.magnificPopup({
            type: 'image',
            gallery: {
                enabled: true
            }
        });
    }
// 12 Pop Up Video
    var popUp = $('.popup-video');
    if (popUp.length) {
        popUp.magnificPopup({
            type: 'iframe'
        });
    }

    /* 13. counterUp*/
    $('.counter').counterUp({
        delay: 10,
        time: 3000
    });

    /* 14. Datepicker */
    $('#datepicker1').datepicker();

// 15. Time Picker
    $('#timepicker').timepicker();

//16. Overlay
    $(".snake").snakeify({
        speed: 200
    });


//17.  Progress barfiller

    $('#bar1').barfiller();
    $('#bar2').barfiller();
    $('#bar3').barfiller();
    $('#bar4').barfiller();
    $('#bar5').barfiller();
    $('#bar6').barfiller();

})(jQuery);
$(document).ready(function ($) {
    var successMessage = $("#jq-notification");
    var notification = $('#notification');
    var warning_notification = $('#warning-jq-notification');

    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');

        }, 3000);
    }
});


// $(document).ready(function() {
//     $('#catalog-search-form').on('submit', function(e) {
//         e.preventDefault();
//         let formData = $(this).serialize();
//         $.ajax({
//                 type: 'GET',
//                 url: '/catalog/api/v1/search/',
//                 data: formData,
//                 success: function (data) {
//                    console.log(data);
//                 }
//             });
//     });
// });
// $(document).ready(function () {
//     // Привязываем обработчик для обеих форм
//     const forms = $('#catalog-search-form-desktop, #catalog-search-form-mobile');
//
//     forms.on('change', function (event) {
//         event.preventDefault();
//
//         const form = $(this); // Текущая форма
//         const formData = form.serializeArray();
//         const params = new URLSearchParams(window.location.search);
//
//         form.find('input[name="price__gte"], input[name="price__lte"]').each(function () {
//             const input = $(this);
//             if (input.val() === '0') {
//                 input.val(''); // Заменяем 0 на пустое значение
//             }
//         });
//
//         // Обновляем параметры URL, явно учитывая состояние чекбоксов
//         form.find('input[type="checkbox"]').each(function () {
//             const checkbox = $(this);
//             const name = checkbox.attr('name');
//             if (!checkbox.is(':checked')) {
//                 params.delete(name); // Удаляем из параметров, если чекбокс не отмечен
//             } else {
//                 params.set(name, checkbox.val()); // Добавляем в параметры, если чекбокс отмечен
//             }
//         });
//
//         // Обновляем остальные параметры формы (например, текстовые поля)
//         formData.forEach(function (item) {
//             if (item.value && item.value !== '0') { // Проверяем, что значение не пустое и не равно 0
//                 params.set(item.name, item.value);
//             } else {
//                 params.delete(item.name); // Удаляем параметр, если значение пустое или равно 0
//             }
//         });
//
//         // Обновляем строку запроса в URL без перезагрузки страницы
//         const newUrl = window.location.pathname + '?' + params.toString();
//         window.history.replaceState({}, '', newUrl);
//         console.log(params);
//
//         // Отправляем AJAX запрос
//         $.ajax({
//             url: '/catalog/api/v1/search/',
//             type: 'GET',
//             data: params.toString(), // Передаем параметры URL в запросе
//             dataType: 'json',
//             success: function (data) {
//                 const coursesList = $('.courses-list');
//                 coursesList.empty();
//                 coursesList.html(data); // Обновляем контент
//             },
//             error: function (xhr, status, error) {
//                 console.error('Ошибка:', error);
//             }
//         });
//     });
// });
// $(document).ready(function () {
//     // Привязываем обработчик для обеих форм
//     const forms = $('#catalog-search-form-desktop, #catalog-search-form-mobile');
//     function resetSelectFields() {
//         forms.find('select').each(function () {
//             $(this).prop('selectedIndex', 0); // Сбрасываем select на первый элемент
//         });
//     }
//     // Функция обновления URL и выполнения поиска
//     function updateSearch(params) {
//         const newUrl = window.location.pathname + '?' + params.toString();
//         window.history.replaceState({}, '', newUrl);
//         console.log(params);
//
//         // Отправляем AJAX запрос
//         $.ajax({
//             url: '/catalog/api/v1/search/',
//             type: 'GET',
//             data: params.toString(), // Передаем параметры URL в запросе
//             dataType: 'json',
//             success: function (data) {
//                 const coursesList = $('.courses-list');
//                 coursesList.empty();
//                 coursesList.html(data); // Обновляем контент
//
//                 // Обновляем кнопки активных фильтров
//                 updateFilterButtons(params);
//                 // Обновляем форму с фильтрами
//                 updateFormFromParams(params);
//             },
//             error: function (xhr, status, error) {
//                 console.error('Ошибка:', error);
//             }
//         });
//     }
//
//     // Функция создания кнопок для активных фильтров
//    function updateFilterButtons(params) {
//     const filterContainer = $('.active-filters');
//     filterContainer.empty(); // Очистка существующих кнопок
//
//     params.forEach((value, key) => {
//         // Проверяем, что значение не пустое и не равно нулю
//         if (value && value !== '0') {
//             const filterButton = $('<button type="button" class=" me-2 mb-2"></button>')
//                 .text(`${key}: ${value} ✕`)
//                 .click(function () {
//                     params.delete(key); // Удаляем фильтр из URL-параметров
//                     updateSearch(params); // Обновляем поиск с новыми параметрами
//                 });
//
//             filterContainer.append(filterButton);
//         }
//     });
// }
//
//
//     // Функция обновления формы на основе параметров URL
//     function updateFormFromParams(params) {
//         // Очищаем значения полей формы
//                 forms.find('input[type="text"], input[type="number"]').val('');
//         forms.find('input[type="checkbox"]').prop('checked', false);
//         forms.find('select').prop('selectedIndex', 0); // Сбрасываем select на первый элемент
//
//         // Применяем параметры из URL к форме
//         params.forEach((value, key) => {
//             const field = forms.find(`[name="${key}"]`);
//
//             if (field.attr('type') === 'checkbox') {
//                 field.prop('checked', true); // Устанавливаем чекбоксы
//             } else if (field.is('select')) {
//                 field.val(value); // Выбираем нужный элемент select
//             } else {
//                 field.val(value); // Устанавливаем значения для текстовых и числовых полей
//             }
//         });
//     }
//
//     // Обработчик изменения формы
//     forms.on('change', function (event) {
//         event.preventDefault();
//
//         const form = $(this);
//         const formData = form.serializeArray();
//         const params = new URLSearchParams(window.location.search);
//
//         form.find('input[name="price__gte"], input[name="price__lte"]').each(function () {
//             const input = $(this);
//             if (input.val() === '0' ) {
//                 input.val(''); // Заменяем 0 на пустое значение
//             }
//         });
//
//         // Обновляем параметры URL, явно учитывая состояние чекбоксов
//         form.find('input[type="checkbox"]').each(function () {
//             const checkbox = $(this);
//             const name = checkbox.attr('name');
//             if (!checkbox.is(':checked')) {
//                 params.delete(name); // Удаляем из параметров, если чекбокс не отмечен
//             } else {
//                 params.set(name, checkbox.val()); // Добавляем в параметры, если чекбокс отмечен
//             }
//         });
//
//         // Обновляем остальные параметры формы (например, текстовые поля)
//         formData.forEach(function (item) {
//             if (item.value && item.value !== '0') { // Проверяем, что значение не пустое и не равно 0
//                 params.set(item.name, item.value);
//             } else {
//                 params.delete(item.name); // Удаляем параметр, если значение пустое или равно 0
//             }
//         });
//
//         updateSearch(params); // Обновляем поиск с новыми параметрами
//     });
//
//     // Инициализация начальных фильтров и формы при загрузке страницы
//     const initialParams = new URLSearchParams(window.location.search);
//     updateFilterButtons(initialParams);
//     updateFormFromParams(initialParams);
// });


// $(document).ready(function () {
//     const forms = $('#catalog-search-form-desktop, #catalog-search-form-mobile');
//
//
//     // Функция обновления URL и выполнения поиска
//     function updateSearch(params) {
//         const newUrl = window.location.pathname + '?' + params.toString();
//         window.history.replaceState({}, '', newUrl);
//         console.log(params);
//
//         // Отправляем AJAX запрос
//         $.ajax({
//             url: '/catalog/api/v1/search/',
//             type: 'GET',
//             data: params.toString(), // Передаем параметры URL в запросе
//             dataType: 'json',
//             success: function (data) {
//                 const coursesList = $('.courses-list');
//                 coursesList.empty();
//                 coursesList.html(data); // Обновляем контент
//
//                 // Обновляем кнопки активных фильтров
//                 updateFilterButtons(params);
//                 // Обновляем форму с фильтрами
//                 updateFormFromParams(params);
//             },
//             error: function (xhr, status, error) {
//                 console.error('Ошибка:', error);
//             }
//         });
//     }
//
// function resetSelectFields() {
//     console.log('reset select');
//
//     // Для кастомного селекта nice-select
//     const languageSelect = forms.find('select[name="language"]');
//
//     // Установите значение для внутреннего HTML селекта
//     const niceSelect = languageSelect.siblings('.nice-select');
//     niceSelect.find('.current').text('Будь-яка мова');
//     niceSelect.find('.option').removeClass('selected');
//     niceSelect.find('.option[data-value=""]').addClass('selected');
//
//     // Обновите значение в оригинальном селекте
//     languageSelect.val('');
// }
//
//
//     // Функция создания кнопок для активных фильтров
//     function updateFilterButtons(params) {
//         const filterContainer = $('.active-filters');
//         filterContainer.empty(); // Очистка существующих кнопок
//
//         let searchInputValueCleared = false; // Флаг для проверки, был ли очищен поле поиска
//
//         params.forEach((value, key) => {
//             if (value && value !== '0') {
//                 const filterButton = $('<button type="button" class=" me-2 mb-2"></button>')
//                     .text(`${key}: ${value} ✕`)
//                     .click(function () {
//                         params.delete(key); // Удаляем фильтр из URL-параметров
//                         updateSearch(params); // Обновляем поиск с новыми параметрами
//                         if (key === 'q') {
//                             $('.search-input').val(''); // Очищаем поле поиска, если фильтр поиска удален
//                             searchInputValueCleared = true;
//                         } else if (key === 'language') {
//                             resetSelectFields(); // Сбрасываем селект, если фильтр языка удален
//                         }
//                     });
//
//                 filterContainer.append(filterButton);
//             }
//         });
//
//         // Если поле поиска очищено, убедитесь, что оно пустое
//         if (searchInputValueCleared) {
//             $('.search-input').val('');
//         }
//     }
//
//     // Функция обновления формы на основе параметров URL
//     function updateFormFromParams(params) {
//         // Очищаем значения полей формы
//         forms.find('input[type="text"], input[type="number"]').val('');
//         forms.find('input[type="checkbox"]').prop('checked', false);
//
//
//         // Применяем параметры из URL к форме
//         params.forEach((value, key) => {
//             const field = forms.find(`[name="${key}"]`);
//
//             if (field.attr('type') === 'checkbox') {
//                 field.prop('checked', true); // Устанавливаем чекбоксы
//             } else if (field.is('select')) {
//                 field.val(value); // Выбираем нужный элемент select
//             } else {
//                 field.val(value); // Устанавливаем значения для текстовых и числовых полей
//             }
//         });
//
//         // Обновляем поле ввода поиска
//         if (params.has('q')) {
//             $('.search-input').val(params.get('q'));
//         } else {
//             $('.search-input').val(''); // Очищаем поле поиска, если параметра 'q' нет
//         }
//     }
//
//     // Обработчик изменения формы
//     forms.on('change', function (event) {
//         event.preventDefault();
//
//         const form = $(this);
//         const formData = form.serializeArray();
//         const params = new URLSearchParams(window.location.search);
//
//         form.find('input[name="price__gte"], input[name="price__lte"]').each(function () {
//             const input = $(this);
//             if (input.val() === '0') {
//                 input.val(''); // Заменяем 0 на пустое значение
//             }
//         });
//
//         // Обновляем параметры URL, явно учитывая состояние чекбоксов
//         form.find('input[type="checkbox"]').each(function () {
//             const checkbox = $(this);
//             const name = checkbox.attr('name');
//             if (!checkbox.is(':checked')) {
//                 params.delete(name); // Удаляем из параметров, если чекбокс не отмечен
//             } else {
//                 params.set(name, checkbox.val()); // Добавляем в параметры, если чекбокс отмечен
//             }
//         });
//
//         // Обновляем остальные параметры формы (например, текстовые поля)
//         formData.forEach(function (item) {
//             if (item.value && item.value !== '0') { // Проверяем, что значение не пустое и не равно 0
//                 params.set(item.name, item.value);
//             } else {
//                 params.delete(item.name); // Удаляем параметр, если значение пустое или равно 0
//             }
//         });
//
//         updateSearch(params); // Обновляем поиск с новыми параметрами
//     });
//
//     // Инициализация начальных фильтров и формы при загрузке страницы
//     const initialParams = new URLSearchParams(window.location.search);
//     updateFilterButtons(initialParams);
//     updateFormFromParams(initialParams);
// });
$(document).ready(function () {

     $('#catalog-search-form-main').on('submit', function (event) {
        event.preventDefault(); // Останавливаем стандартное поведение формы

        const form = $(this);
        const formData = form.serializeArray();
        const params = new URLSearchParams(window.location.search);

        // Удаляем параметр 'q' из текущих параметров, если он есть
        params.delete('q');

        // Добавляем все параметры из формы, кроме 'q'
        formData.forEach(({ name, value }) => {
            if (name !== 'q') {
                params.set(name, value);
            }
        });

        // Добавляем новый параметр 'q' из формы
        const searchQuery = form.find('input[name="q"]').val();
        if (searchQuery) {
            params.set('q', searchQuery);
        }

        // Создаем новый URL и перенаправляем
        const newUrl = `${window.location.pathname}?${params.toString()}`;
        window.location.href = newUrl;
    });

    const forms = $('#catalog-search-form-desktop, #catalog-search-form-mobile');

    function updateSearch(params) {
        const newUrl = `${window.location.pathname}?${params.toString()}`;
        window.history.replaceState({}, '', newUrl);

        $.ajax({
            url: '/catalog/api/v1/search/',
            type: 'GET',
            data: params.toString(),
            dataType: 'json',
            success: function (data) {
                $('.courses-list').empty().html(data);
                updateFilterButtons(params);
                updateFormFromParams(params);
            },
            error: function (xhr, status, error) {
                console.error('Ошибка:', error);
            }
        });
    }

    function resetSelectFields(fieldName) {
    const select = forms.find(`select[name="${fieldName}"]`);
    const niceSelect = select.siblings('.nice-select');
    niceSelect.find('.current').text('Всі') // Можно заменить на более общий текст, если нужно
        .end().find('.option').removeClass('selected')
        .filter('[data-value=""]').addClass('selected');
    select.val('');
}

    // function updateFilterButtons(params) {
    //     const filterContainer = $('.active-filters').empty();
    //     let searchInputCleared = false;
    //
    //     params.forEach((value, key) => {
    //         if (value && value !== '0') {
    //             $('<button type="button" class="button-3 m-0 me-2 mb-2" style="width: 100px; height: 40px"></button>')
    //                 .text(`${value} ✕`)
    //                 .click(function () {
    //                     params.delete(key);
    //                     updateSearch(params);
    //                     if (key === 'q') {
    //                         $('.search-input').val('');
    //                         searchInputCleared = true;
    //                     } else if (key === 'language') {
    //                         resetSelectFields();
    //                     }
    //                 })
    //                 .appendTo(filterContainer);
    //         }
    //     });
    //
    //     if (searchInputCleared) $('.search-input').val('');
    // }
     function updateFilterButtons(params) {
        const filterContainer = $('.active-filters').empty();
        let searchInputCleared = false;

        params.forEach((value, key) => {
            if (value && value !== '0') {
                let displayText = value;
                const element = $(`input[name="${key}"], select[name="${key}"]`);

                if (element.length) {
                    // Для селектов ищем значение в опциях
                    if (element.is('select')) {
                        const option = element.find(`option[value="${value}"]`);
                        displayText = option.data('btn-label') || option.text();
                    } else {
                        displayText = element.data('btn-label') || value;
                        if (key.startsWith('price')) {
                            displayText = `${element.data('btn-label')} ${value}`;
                        }
                    }
                }

                $('<button>', {
                    type: 'button',
                    class: 'button-3 m-0 me-2 mb-2',
                    style:  'height: 35px',
                    text: `${displayText} ✕`,
                    click: function () {
                        params.delete(key);
                        updateSearch(params);
                        if (key === 'q') {
                            $('.search-input').val('');
                            searchInputCleared = true;
                        } else if (key === 'language' || key === 'difficulty') {
                            resetSelectFields(key);
                        }
                    }
                }).appendTo(filterContainer);
            }
        });

        if (searchInputCleared) $('.search-input').val('');
    }


    function updateFormFromParams(params) {
        forms.find('input[type="text"], input[type="number"]').val('')
            .end().find('input[type="checkbox"]').prop('checked', false);

        params.forEach((value, key) => {
            const field = forms.find(`[name="${key}"]`);
            if (field.is('select')) {
                field.val(value);
            } else if (field.attr('type') === 'checkbox') {
                field.prop('checked', true);
            } else {
                field.val(value);
            }
        });

        $('.search-input').val(params.get('q') || '');
    }

    forms.on('change', function (event) {
        event.preventDefault();
        const form = $(this);
        const formData = form.serializeArray();
        const params = new URLSearchParams(window.location.search);

        form.find('input[name="price__gte"], input[name="price__lte"]').val(function (_, value) {
            return value === '0' ? '' : value;
        });

        form.find('input[type="checkbox"]').each(function () {
            const checkbox = $(this);
            const name = checkbox.attr('name');
            checkbox.is(':checked') ? params.set(name, checkbox.val()) : params.delete(name);
        });

        formData.forEach(({ name, value }) => {
            value && value !== '0' ? params.set(name, value) : params.delete(name);
        });

        updateSearch(params);
    });

    updateFilterButtons(new URLSearchParams(window.location.search));
    updateFormFromParams(new URLSearchParams(window.location.search));
});
