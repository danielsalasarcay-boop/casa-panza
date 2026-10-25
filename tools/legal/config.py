# Contenido de las páginas legales de Casa Panza (terminos.html, privacidad.html, cookies.html).
# Regenerar: python3 tools/legal/legalgen.py tools/legal/config.py .
# Al cambiar un texto de fondo, sube VERSION y la fecha de UPDATED.
#
# PENDIENTE (lo da el dueño): razón social y RIF del titular, y correo de contacto.
# Cuando estén, añadirlos en "Quiénes somos" (Términos) y "Responsable" (Privacidad).

VERSION = "2026-10-25"
WA = '<a href="https://wa.me/584123030330">+58 412-303-0330</a>'

SITE = {
    "name": "Casa Panza",
    "brand_html": "Casa Panza",
    "kicker": {"es": "Casa Panza · Gran Roque", "en": "Casa Panza · Gran Roque"},
    "langs": ["es", "en"],
    "lang_key": "lang",
    "home": {"es": "index.html", "en": "index.html"},
    "files": {"terms": "terminos.html", "privacy": "privacidad.html", "cookies": "cookies.html"},
    "version": VERSION,
    "updated": {"es": "25 de octubre de 2026", "en": "October 25, 2026"},
    "head": '<link rel="icon" type="image/svg+xml" href="favicon.svg">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">',
    "style": {
        "bg": "#FFFFFF", "ink": "#1A1A1A", "muted": "#6B6B6B", "accent": "#1C8C8C", "line": "#E8E2D8", "card": "#F8F7F5",
        "display": "'Cormorant Garamond', Georgia, serif", "body": "'Jost', system-ui, sans-serif",
        "brand_size": "22px", "brand_track": "0.22em", "brand_case": "uppercase", "h_weight": "500",
    },
}

DOCS = {
    "terms": {
        "es": {
            "title": "Términos y condiciones",
            "description": "Condiciones de uso del sitio de Casa Panza y de las reservas de estadía en Gran Roque, Los Roques.",
            "intro": ["Estos términos regulan el uso de este sitio web y las solicitudes y reservas de estadía en Casa Panza, casa vacacional ubicada en Gran Roque, Parque Nacional Archipiélago Los Roques, Venezuela. Al usar el sitio o solicitar una reserva, aceptas estos términos."],
            "sections": [
                ("1. Quiénes somos", [
                    f"Casa Panza es una casa vacacional en Gran Roque, Los Roques, Venezuela. Contacto: WhatsApp {WA}.",
                ]),
                ("2. Qué ofrecemos", [
                    "Casa Panza se alquila como casa completa para estadías vacacionales, para un máximo de 10 huéspedes, con los servicios que se describen en el sitio (staff, limpieza diaria y chef privado, entre otros). Los servicios incluidos, el precio, los horarios de entrada y salida y las condiciones de cada estadía son los que indica la confirmación de reserva.",
                ]),
                ("3. Cómo se reserva", [[
                    "Los botones del sitio abren una conversación de WhatsApp. Escribirnos es una consulta: no es una reserva ni genera ningún pago.",
                    "La reserva queda confirmada cuando te enviamos por escrito (WhatsApp o correo) la confirmación con fechas, número de huéspedes, precio total, servicios incluidos, forma de pago y condiciones de cancelación, y recibimos el pago o el anticipo que ella indique. Al pagar aceptas esa confirmación y estos términos.",
                    "Para confirmar la reserva te pediremos solo los datos necesarios: nombre completo, documento de identidad o pasaporte de los huéspedes, cuando lo exija la ley o la autoridad del Parque Nacional, y los datos del pago.",
                    "Las comunicaciones y aceptaciones por medios electrónicos (WhatsApp o correo) tienen plena validez, conforme a la Ley sobre Mensajes de Datos y Firmas Electrónicas.",
                    "Quien reserva debe ser mayor de edad y responde por el grupo de huéspedes.",
                ]]),
                ("4. Precios y pagos", [[
                    "El precio de cada estadía es el que indica la confirmación de reserva, en dólares estadounidenses y su equivalente en bolívares a la tasa oficial del Banco Central de Venezuela del día del pago, conforme a la normativa vigente.",
                    "Los pagos en divisas pueden estar sujetos al Impuesto a las Grandes Transacciones Financieras (IGTF) cuando la ley lo exija.",
                    "Salvo que la confirmación diga otra cosa, el precio no incluye boletos aéreos ni traslados hasta Los Roques, ni la tasa de ingreso al Parque Nacional que cobra la autoridad competente.",
                ]]),
                ("5. Cancelaciones y cambios", [
                    "Las cancelaciones, los cambios de fecha y los reembolsos se rigen por las condiciones indicadas en la confirmación de reserva, que conoces y aceptas antes de pagar.",
                    "Si Casa Panza tuviera que cancelar una reserva confirmada por una causa que no sea tuya, te devolveremos el 100 % de lo pagado o, si lo prefieres, reprogramaremos la estadía según disponibilidad.",
                ]),
                ("6. Normas de la estadía", [[
                    "No se admite un número de huéspedes mayor al confirmado.",
                    "Los huéspedes deben respetar las normas del Parque Nacional Archipiélago Los Roques y de sus autoridades, en especial sobre fauna, arrecifes, residuos y pesca.",
                    "Los huéspedes responden por los daños que causen a la casa, su mobiliario o equipos, más allá del desgaste normal. Podrá pedirse un depósito de garantía si así lo indica la confirmación.",
                ]]),
                ("7. Fuerza mayor", [
                    "Ninguna de las partes responde por incumplimientos causados por hechos ajenos a su control que no pudo prever ni evitar (causa extraña no imputable, artículo 1.272 del Código Civil): suspensión de vuelos, cierre del acceso al Parque Nacional, condiciones climáticas, cortes de electricidad o de comunicaciones, emergencias sanitarias o decisiones de autoridades. Si ocurre, te avisaremos lo antes posible y buscaremos contigo reprogramar la estadía; las consecuencias económicas se resuelven según la confirmación de reserva y la ley.",
                ]),
                ("8. Fotos y contenido del sitio", [
                    "Las fotografías muestran la casa y su entorno. Algunas tienen retoques digitales de luz, color o nitidez y son ilustrativas: la decoración, el mobiliario y la vista pueden variar según la temporada y el momento del día.",
                    "Los textos, fotos, logotipo y diseño del sitio pertenecen a Casa Panza o se usan con autorización. No pueden copiarse ni reutilizarse sin permiso escrito.",
                ]),
                ("9. Servicios de terceros", [
                    "El sitio enlaza con WhatsApp y muestra un mapa de Google Maps. Esos servicios se rigen por sus propias condiciones y políticas de privacidad.",
                ]),
                ("10. Responsabilidad", [
                    "Hacemos lo posible para que la información del sitio sea exacta y esté actualizada, pero la disponibilidad, los precios y los servicios solo son vinculantes en la confirmación escrita. Nada de lo aquí escrito limita los derechos que la ley te reconoce como consumidor, que son irrenunciables.",
                ]),
                ("11. Ley aplicable y reclamos", [
                    "Estos términos se rigen por las leyes de la República Bolivariana de Venezuela. Si tienes un reclamo, escríbenos primero por WhatsApp y te responderemos en un plazo máximo de 10 días hábiles. También puedes acudir a la Superintendencia Nacional para la Defensa de los Derechos Socioeconómicos (SUNDDE) o a los tribunales competentes.",
                ]),
                ("12. Cambios", [
                    "Podemos actualizar estos términos. La versión vigente es la publicada en esta página con su fecha; cada reserva se rige por la versión vigente cuando fue confirmada.",
                ]),
            ],
        },
        "en": {
            "title": "Terms and conditions",
            "description": "Terms of use of the Casa Panza website and of stay bookings in Gran Roque, Los Roques.",
            "intro": ["These terms govern the use of this website and stay requests and bookings at Casa Panza, a vacation home in Gran Roque, Archipiélago Los Roques National Park, Venezuela. By using the site or requesting a booking, you accept these terms. The Spanish version prevails in case of discrepancy."],
            "sections": [
                ("1. Who we are", [
                    f"Casa Panza is a vacation home in Gran Roque, Los Roques, Venezuela. Contact: WhatsApp {WA}.",
                ]),
                ("2. What we offer", [
                    "Casa Panza is rented as a whole house for vacation stays, for up to 10 guests, with the services described on the site (staff, daily cleaning and a private chef, among others). The included services, price, check-in and check-out times and conditions of each stay are those stated in the booking confirmation.",
                ]),
                ("3. How to book", [[
                    "The site's buttons open a WhatsApp conversation. Writing to us is an inquiry: it is not a booking and involves no payment.",
                    "A booking is confirmed when we send you a written confirmation (WhatsApp or email) with dates, number of guests, total price, included services, payment method and cancellation conditions, and we receive the payment or deposit it states. By paying you accept that confirmation and these terms.",
                    "To confirm the booking we will only ask for the necessary data: full name, ID or passport of the guests when required by law or by the National Park authority, and payment details.",
                    "Electronic communications and acceptances (WhatsApp or email) are fully valid under Venezuela's Law on Data Messages and Electronic Signatures.",
                    "The person booking must be of legal age and is responsible for the group of guests.",
                ]]),
                ("4. Prices and payments", [[
                    "The price of each stay is the one stated in the booking confirmation, in US dollars and its equivalent in bolívares at the official Central Bank of Venezuela rate on the payment date, as required by law.",
                    "Payments in foreign currency may be subject to the Large Financial Transactions Tax (IGTF) when required by law.",
                    "Unless the confirmation says otherwise, the price does not include flights or transfers to Los Roques, nor the National Park entry fee charged by the authorities.",
                ]]),
                ("5. Cancellations and changes", [
                    "Cancellations, date changes and refunds are governed by the conditions stated in the booking confirmation, which you know and accept before paying.",
                    "If Casa Panza has to cancel a confirmed booking for a reason not attributable to you, we will refund 100% of what you paid or, if you prefer, reschedule the stay subject to availability.",
                ]),
                ("6. House rules", [[
                    "No more guests than confirmed are allowed.",
                    "Guests must follow the rules of the Archipiélago Los Roques National Park and its authorities, especially regarding wildlife, reefs, waste and fishing.",
                    "Guests are liable for damage they cause to the house, its furniture or equipment beyond normal wear. A security deposit may be requested if the confirmation says so.",
                ]]),
                ("7. Force majeure", [
                    "Neither party is liable for failures caused by events beyond its control that it could not foresee or avoid (article 1,272 of the Venezuelan Civil Code): flight suspensions, closure of access to the National Park, weather conditions, power or communication outages, health emergencies or decisions of authorities. If this happens, we will notify you as soon as possible and work with you to reschedule; the financial consequences are settled according to the booking confirmation and the law.",
                ]),
                ("8. Photos and site content", [
                    "The photographs show the house and its surroundings. Some have digital adjustments to light, color or sharpness and are illustrative: decoration, furniture and views may vary with the season and time of day.",
                    "The texts, photos, logo and design of the site belong to Casa Panza or are used with permission. They may not be copied or reused without written permission.",
                ]),
                ("9. Third-party services", [
                    "The site links to WhatsApp and shows a Google Maps map. Those services are governed by their own terms and privacy policies.",
                ]),
                ("10. Liability", [
                    "We do our best to keep the site's information accurate and up to date, but availability, prices and services are only binding in the written confirmation. Nothing here limits the rights the law grants you as a consumer, which cannot be waived.",
                ]),
                ("11. Governing law and complaints", [
                    "These terms are governed by the laws of the Bolivarian Republic of Venezuela. If you have a complaint, write to us first on WhatsApp and we will reply within 10 business days. You may also turn to the National Superintendence for the Defense of Socioeconomic Rights (SUNDDE) or the competent courts.",
                ]),
                ("12. Changes", [
                    "We may update these terms. The current version is the one published on this page with its date; each booking is governed by the version in force when it was confirmed.",
                ]),
            ],
        },
    },
    "privacy": {
        "es": {
            "title": "Política de privacidad",
            "description": "Qué datos trata Casa Panza, para qué, con quién se comparten y cómo ejercer tus derechos.",
            "intro": ["Aquí te contamos qué datos tuyos usamos, para qué, cuánto tiempo los guardamos y cómo puedes pedir que los cambiemos o borremos. Respetamos el derecho a la privacidad y a la protección de datos que reconoce la Constitución de Venezuela (artículos 28 y 60)."],
            "sections": [
                ("1. Responsable", [
                    f"Casa Panza, casa vacacional en Gran Roque, Los Roques, Venezuela, es responsable de los datos que nos das. Para cualquier pregunta sobre tus datos, escríbenos por WhatsApp al {WA}.",
                ]),
                ("2. Qué datos tratamos y para qué", [
                    "El sitio no tiene formularios ni registro de usuarios, no usa cookies propias ni herramientas de analítica o publicidad, y no guarda en ningún servidor información sobre ti. Solo tratamos lo que tú decides enviarnos:",
                    ("table", ["Cuándo", "Datos", "Para qué"], [
                        ["Si nos escribes por WhatsApp", "Tu número, tu nombre de perfil y lo que nos escribas.", "Responder tu consulta y gestionar la reserva."],
                        ["Si reservas", "Nombre completo, documento de identidad o pasaporte de los huéspedes (cuando lo exija la ley o la autoridad del Parque) y datos del pago.", "Ejecutar la reserva y cumplir obligaciones legales y fiscales."],
                        ["Al visitar el sitio", "Datos técnicos de conexión (dirección IP, navegador) que reciben el alojamiento y los proveedores de contenido.", "Entregar la página de forma segura. Casa Panza no accede a ellos."],
                    ]),
                    "Usamos tus datos con tu consentimiento, que das al escribirnos, y para ejecutar la reserva cuando la confirmas. No vendemos datos, no los usamos para publicidad y no te enviaremos mensajes promocionales sin tu permiso.",
                ]),
                ("3. Con quién se comparten", [
                    "Solo con los servicios necesarios para que el sitio funcione y para atenderte, y con las autoridades cuando la ley lo exija:",
                    [
                        "Meta (WhatsApp), para las conversaciones que inicias.",
                        "Vercel y GitHub (alojamiento del sitio).",
                        "Google (fuentes tipográficas y mapa de Google Maps), cdnjs y jsDelivr (archivos de diseño y animación), que reciben datos técnicos de conexión, como la IP, para entregar la página.",
                        "Autoridades públicas cuando una ley lo exija (por ejemplo, registro de huéspedes o requerimientos fiscales).",
                    ],
                    "Algunos de estos proveedores procesan datos fuera de Venezuela, principalmente en Estados Unidos.",
                ]),
                ("4. Cuánto tiempo los guardamos", [[
                    "Conversaciones que no terminan en reserva: hasta 12 meses.",
                    "Datos de reservas y pagos: el tiempo que exija la normativa tributaria y mercantil.",
                ]]),
                ("5. Tus derechos", [
                    "Puedes pedir en cualquier momento saber qué datos tenemos sobre ti y para qué, que los actualicemos, corrijamos o eliminemos, y retirar tu consentimiento, sin efecto sobre lo hecho antes. Escríbenos por WhatsApp; responderemos en un máximo de 15 días hábiles. Si pides eliminar tus datos, solo conservaremos lo que exija la ley. Si resides en la Unión Europea, también puedes reclamar ante la autoridad de protección de datos de tu país.",
                ]),
                ("6. Seguridad y menores", [
                    "El sitio funciona con conexión cifrada (HTTPS) y las conversaciones contigo solo las atiende Casa Panza. El sitio no está dirigido a menores de 18 años; las reservas deben hacerlas personas mayores de edad.",
                ]),
                ("7. Cambios", [
                    "Si cambiamos esta política, publicaremos la nueva versión en esta página con su fecha.",
                ]),
            ],
        },
        "en": {
            "title": "Privacy policy",
            "description": "What data Casa Panza processes, why, who it is shared with and how to exercise your rights.",
            "intro": ["Here we explain what data of yours we use, why, how long we keep it and how you can ask us to change or delete it. We respect the rights to privacy and data protection recognized by the Venezuelan Constitution (articles 28 and 60). The Spanish version prevails in case of discrepancy."],
            "sections": [
                ("1. Controller", [
                    f"Casa Panza, a vacation home in Gran Roque, Los Roques, Venezuela, is responsible for the data you give us. For any question about your data, write to us on WhatsApp at {WA}.",
                ]),
                ("2. What data we process and why", [
                    "The site has no forms or user accounts, uses no first-party cookies or analytics or advertising tools, and does not store any information about you on any server. We only process what you choose to send us:",
                    ("table", ["When", "Data", "Purpose"], [
                        ["If you write to us on WhatsApp", "Your number, profile name and what you write.", "Answer your inquiry and manage the booking."],
                        ["If you book", "Full name, ID or passport of the guests (when required by law or the Park authority) and payment details.", "Carry out the booking and meet legal and tax obligations."],
                        ["When you visit the site", "Technical connection data (IP address, browser) received by the hosting and content providers.", "Deliver the page securely. Casa Panza does not access it."],
                    ]),
                    "We use your data with your consent, which you give by writing to us, and to perform the booking once you confirm it. We do not sell data, use it for advertising or send you promotional messages without your permission.",
                ]),
                ("3. Who we share it with", [
                    "Only with the services needed for the site to work and to assist you, and with authorities when required by law:",
                    [
                        "Meta (WhatsApp), for the conversations you start.",
                        "Vercel and GitHub (site hosting).",
                        "Google (fonts and the Google Maps map), cdnjs and jsDelivr (design and animation files), which receive technical connection data, such as your IP, to deliver the page.",
                        "Public authorities when required by law (for example, guest registration or tax requests).",
                    ],
                    "Some of these providers process data outside Venezuela, mainly in the United States.",
                ]),
                ("4. How long we keep it", [[
                    "Conversations that do not lead to a booking: up to 12 months.",
                    "Booking and payment data: as long as tax and commercial law requires.",
                ]]),
                ("5. Your rights", [
                    "At any time you may ask what data we hold about you and why, have it updated, corrected or deleted, and withdraw your consent, without affecting what was done before. Write to us on WhatsApp; we will reply within 15 business days. If you ask us to delete your data, we will only keep what the law requires. If you live in the European Union, you may also complain to your country's data protection authority.",
                ]),
                ("6. Security and minors", [
                    "The site uses an encrypted connection (HTTPS) and conversations with you are handled only by Casa Panza. The site is not aimed at people under 18; bookings must be made by adults.",
                ]),
                ("7. Changes", [
                    "If we change this policy, we will publish the new version on this page with its date.",
                ]),
            ],
        },
    },
    "cookies": {
        "es": {
            "title": "Política de cookies",
            "description": "Casa Panza no usa cookies propias. Qué guarda tu navegador y qué cookies puede poner el mapa de Google.",
            "intro": ["Las cookies son pequeños archivos que un sitio guarda en tu navegador. Esta página explica qué se guarda al visitar Casa Panza."],
            "sections": [
                ("1. Cookies propias", [
                    "Casa Panza no usa cookies propias, ni de analítica ni de publicidad. Solo guarda en tu navegador una preferencia técnica, que no te identifica y no sale de tu dispositivo:",
                    ("table", ["Nombre", "Para qué", "Duración"], [
                        ["lang (almacenamiento local)", "Recordar el idioma que elegiste (español o inglés).", "Hasta que la borres."],
                    ]),
                ]),
                ("2. Google Maps", [
                    'El mapa de la sección Ubicación lo presta Google Maps. Al cargarse, Google puede instalar sus propias cookies y recibir datos técnicos como tu IP. Casa Panza no accede a esas cookies. Si no quieres que se instalen, puedes bloquear las cookies de terceros en tu navegador. Más información en la <a href="https://policies.google.com/technologies/cookies?hl=es" rel="noopener">política de cookies de Google</a>.',
                ]),
                ("3. Fuentes y archivos externos", [
                    "Las tipografías (Google Fonts) y algunos archivos de diseño y animación (cdnjs, jsDelivr) se descargan de servicios externos. No instalan cookies, pero reciben datos técnicos de conexión, como la IP, para entregarlos.",
                ]),
                ("4. WhatsApp", [
                    "Los botones de WhatsApp son enlaces normales: no cargan nada de ese servicio hasta que los pulsas. A partir de ahí aplican sus propias políticas.",
                ]),
                ("5. Cómo controlarlas", [
                    "Puedes borrar el almacenamiento y bloquear o borrar cookies desde la configuración de tu navegador; el sitio seguirá funcionando.",
                ]),
            ],
        },
        "en": {
            "title": "Cookie policy",
            "description": "Casa Panza uses no first-party cookies. What your browser stores and which cookies the Google map may set.",
            "intro": ["Cookies are small files a website stores in your browser. This page explains what is stored when you visit Casa Panza. The Spanish version prevails in case of discrepancy."],
            "sections": [
                ("1. First-party cookies", [
                    "Casa Panza uses no first-party cookies, for analytics or advertising. It only stores one technical preference in your browser, which does not identify you and never leaves your device:",
                    ("table", ["Name", "Purpose", "Duration"], [
                        ["lang (local storage)", "Remember the language you chose (Spanish or English).", "Until you delete it."],
                    ]),
                ]),
                ("2. Google Maps", [
                    'The map in the Location section is provided by Google Maps. When it loads, Google may set its own cookies and receive technical data such as your IP. Casa Panza has no access to those cookies. If you do not want them, you can block third-party cookies in your browser. More information in <a href="https://policies.google.com/technologies/cookies?hl=en" rel="noopener">Google\'s cookie policy</a>.',
                ]),
                ("3. External fonts and files", [
                    "The fonts (Google Fonts) and some design and animation files (cdnjs, jsDelivr) are downloaded from external services. They set no cookies but receive technical connection data, such as your IP, to deliver them.",
                ]),
                ("4. WhatsApp", [
                    "The WhatsApp buttons are plain links: nothing from that service loads until you tap them. From then on, its own policies apply.",
                ]),
                ("5. How to control them", [
                    "You can clear storage and block or delete cookies in your browser settings; the site will keep working.",
                ]),
            ],
        },
    },
}
