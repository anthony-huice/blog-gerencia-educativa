# -*- coding: utf-8 -*-
"""
Auditor y Humanizador de Blog Académico
Elimina andamiaje de IA, meta-etiquetas de prompt, clichés sintácticos y léxico artificial.
Mantiene rigor académico, normas APA 7, 3 etiquetas exactas,
recursos multimedia funcionales y extensión de 610-670 palabras por entrada.
"""

import os
import re

POSTS = [
    {
        "id": 1,
        "date": "2026-11-06T23:59:00Z",
        "title": "Fundamentos teóricos y liderazgo situacional en la gerencia educativa",
        "tags": ["GerenciaEducativa", "PodcastPedagogico", "LiderazgoSituacional"],
        "image_url": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Micrófono de estudio para grabación de podcast educativo",
        "paragraphs_part1": [
            "En la cuarta unidad de nuestro programa formativo, el análisis se concentra en las bases epistemológicas de la administración escolar y en el papel del liderazgo directivo frente a los cambios tecnológicos. La discusión cobra relevancia práctica al observar cómo muchas instituciones educativas intentan aplicar esquemas gerenciales del sector comercial sin considerar que los objetivos, los procesos y los actores del ámbito escolar responden a lógicas sociales y pedagógicas muy distintas.",
            "En el podcast correspondiente a esta unidad, la Lic. Emily Leidy Chacón de Romero (Centro Local Anzoátegui, Universidad Nacional Abierta) examina los principios que diferencian a la gerencia educativa de la administración general. Mientras la empresa privada suele priorizar la rentabilidad financiera y la optimización de costes, la institución formativa orienta su gestión hacia la calidad del aprendizaje, la equidad en el acceso al conocimiento y el desarrollo integral de la persona (Chiavenato, 2014).",
            "Esta distinción se apoya en varias corrientes teóricas complementarias. La teoría clásica aporta pautas para la división del trabajo, la asignación de responsabilidades y la estructura organizativa básica del plantel. La teoría humanista sitúa la atención en el clima institucional, la motivación del profesorado y las relaciones interpersonales, elementos determinantes para el compromiso docente. Por su parte, el enfoque sistémico permite concebir a la escuela como un sistema abierto en constante interacción con las familias y la comunidad, mientras que la perspectiva socio-pedagógica recuerda que cualquier decisión administrativa debe justificarse en función de su impacto en la formación de los estudiantes (Fullan, 2016; UPEL, 2016)."
        ],
        "multimedia_type": "audio",
        "paragraphs_part2": [
            "Un aspecto central del análisis de la Lic. Chacón es la revisión de los modelos de gestión presentes en el sistema educativo. El modelo normativo tradicional, centrado en el cumplimiento estricto de reglamentos y en la supervisión vertical, muestra serias limitaciones cuando las instituciones deben adaptarse a entornos virtuales o responder a contingencias imprevistas. Frente a esta rigidez, modelos como el estratégico-situacional, el prospectivo o el comunicacional ofrecen herramientas más flexibles para negociar prioridades, planificar por escenarios y construir acuerdos con la comunidad académica.",
            "De este recorrido conceptual se desprende que el directivo escolar difícilmente puede apoyarse en una sola fórmula de gestión. Como señalan Hersey y Blanchard (1988), el liderazgo situacional permite ajustar las pautas de supervisión y apoyo según la experiencia del equipo docente y las características de cada proyecto. En centros educativos que integran tecnologías digitales, esta capacidad de adaptación facilita que las decisiones técnicas se alineen con las necesidades pedagógicas reales de las aulas.",
            "El fortalecimiento de la gestión educativa requiere directivos capaces de combinar la claridad operativa con una visión humana del trabajo institucional. Frente a los desafíos actuales de nuestras escuelas y universidades, cabe preguntarse: ¿hasta qué punto predomina aún en nuestras instituciones un enfoque burocrático tradicional, y qué condiciones prácticas se necesitan para consolidar un liderazgo situacional en el día a día académico?"
        ],
        "references": [
            "Chacón de Romero, E. L. (2026). <em>Aspectos fundamentales de la gerencia educativa: De las bases teóricas al liderazgo situacional</em> [Episodio de podcast de audio]. Vocaroo. <a href=\"https://voca.ro/143LDvk3Ro19\" target=\"_blank\" rel=\"noopener\">https://voca.ro/143LDvk3Ro19</a>",
            "Chiavenato, I. (2014). <em>Comportamiento organizacional: La dinámica del éxito en las organizaciones</em> (3.ª ed.). McGraw-Hill Educación.",
            "Fullan, M. (2016). <em>The new meaning of educational change</em> (5th ed.). Teachers College Press.",
            "Hersey, P., & Blanchard, K. H. (1988). <em>Management of organizational behavior: Utilizing human resources</em> (5th ed.). Prentice-Hall.",
            "Universidad Pedagógica Experimental Libertador [UPEL]. (2016). <em>Manual de trabajos de grado de especialización y maestría y tesis doctorales</em> (5.ª ed.). FEDUPEL."
        ]
    },
    {
        "id": 2,
        "date": "2026-11-05T20:00:00Z",
        "title": "Canales síncronos y asíncronos en el diseño de cursos virtuales",
        "tags": ["ComunicacionDigital", "PresenciaCognitiva", "AprendizajeMezclado"],
        "image_url": "https://images.unsplash.com/photo-1588196749597-9ff075ee6b5b?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Estudiante en sesión de trabajo virtual con ordenador portátil",
        "paragraphs_part1": [
            "La planificación de la comunicación en la educación a distancia representa una de las tareas más delicadas para los coordinadores académicos y diseñadores instruccionales. Con frecuencia, las dificultades que experimentan los cursos en línea se atribuyen a problemas de conectividad o desinterés del alumnado, cuando en realidad derivan de una combinación deficiente entre los momentos de encuentro en tiempo real y las actividades de trabajo independiente.",
            "En la video-exposición desarrollada durante la Unidad 2, analizamos las funciones pedagógicas de los canales síncronos y asíncronos en los entornos virtuales de aprendizaje. Las herramientas síncronas, como las salas de videoconferencia y las sesiones de chat programadas, resultan útiles para generar sentido de pertenencia grupal, atender dudas complejas de forma inmediata y propiciar debates directos entre profesores y estudiantes (Garrison et al., 2000).",
            "Sin embargo, el empleo excesivo de sesiones en directo genera problemas concretos: rigidez horaria para quienes trabajan, saturación por exposición continua a pantallas y exclusión de estudiantes con conexiones inestables. Por el contrario, los canales asíncronos —como los foros de debate moderados, las wikis temáticas y la mensajería en plataforma— permiten que los estudiantes organicen sus tiempos de estudio, revisen lecturas con mayor calma y preparen aportes argumentados con mayor profundidad (Moore, 1993)."
        ],
        "multimedia_type": "video",
        "paragraphs_part2": [
            "La integración equilibrada de ambos formatos constituye la base del aprendizaje combinado o <em>blended learning</em>. En modelos como el aula invertida, los contenidos teóricos y las lecturas analíticas se abordan de manera asincrónica, mientras que las sesiones en tiempo real se reservan para talleres de resolución de problemas, estudios de caso y asesorías puntuales (Bates, 2019). De esta forma, el tiempo compartido entre docente y estudiantes adquiere un valor formativo superior al de la clase expositiva tradicional.",
            "Esta organización requiere que el profesorado desarrolle competencias para la curaduría de contenidos y la moderación pedagógica de foros virtuales. No basta con colgar lecturas en formato PDF; es necesario pautar consignas claras, retroalimentar oportunamente las intervenciones de los estudiantes y evitar que la interacción virtual se diluya por falta de acompañamiento docente.",
            "Para lograr una articulación efectiva entre ambas modalidades, los equipos docentes deben establecer pautas explícitas desde el inicio del período académico. El estudiante a distancia necesita conocer con exactitud qué peso evaluativo tienen los foros de discusión, cuáles son los criterios de calidad esperados en sus intervenciones escritas y en qué momentos específicos se realizarán los encuentros sincrónicos. La claridad en el diseño instruccional reduce la ansiedad de los participantes y favorece un clima de aprendizaje propicio para el intercambio intelectual riguroso y la construcción colectiva de saberes entre todos los integrantes del curso.",
            "Al diseñar un programa formativo a distancia, la selección de herramientas tecnológicas debe supeditarse al propósito didáctico de cada contenido. Ante esta realidad, surge una pregunta para quienes coordinan asignaturas en línea: ¿qué criterios pedagógicos específicos utiliza su institución para decidir cuándo una actividad debe ser síncrona y cuándo asíncrona, garantizando el rigor académico sin sobrecargar el tiempo de estudio de los participantes?"
        ],
        "references": [
            "Bates, A. W. (2019). <em>Teaching in a digital age: Guidelines for designing teaching and learning</em> (2nd ed.). Tony Bates Associates Ltd.",
            "Garrison, D. R., Anderson, T., & Archer, W. (2000). Critical inquiry in a text-based environment: Computer conferencing in higher education. <em>The Internet and Higher Education</em>, 2(2-3), 87–105.",
            "Moore, M. G. (1993). Theory of transactional distance. En D. Keegan (Ed.), <em>Theoretical principles of distance education</em> (pp. 22–38). Routledge.",
            "Universidad Pedagógica Experimental Libertador [UPEL]. (2016). <em>Manual de trabajos de grado</em>. FEDUPEL."
        ]
    },
    {
        "id": 3,
        "date": "2026-11-04T18:00:00Z",
        "title": "Liderazgo transformacional y gestión del cambio en instituciones educativas",
        "tags": ["LiderazgoEducativo", "TransformacionDigital", "GestionEscolar"],
        "image_url": "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Equipo directivo docente en reunión de trabajo institucional",
        "paragraphs_part1": [
            "La incorporación de tecnologías en los centros de enseñanza suele entenderse como un proceso de adquisición de equipos informáticos y licencias de software. No obstante, las evaluaciones de proyectos de modernización educativa en América Latina revelan que las principales barreras no son presupuestarias, sino de cultura organizativa y estilos de dirección (UNESCO, 2023). Cuando los directivos aplican criterios de control burocrático sobre entornos digitales, la innovación suele reducirse al trámite documental.",
            "El modelo administrativo clásico coloca el acento en la supervisión formal, el apego estricto a directrices superiores y la estandarización de procedimientos. Si bien este enfoque aporta orden administrativo, tiende a inhibir la iniciativa de los docentes y genera resistencia frente a propuestas metodológicas novedosas. Como señalan Bass y Avolio (1994), las instituciones escolares que buscan renovar sus prácticas formativas necesitan transitar hacia un liderazgo transformacional, caracterizado por la motivación del personal, el respaldo a la experimentación docente y la construcción de metas compartidas.",
            "El rol de la dirección escolar no consiste en prescribir herramientas digitales por decreto, sino en crear condiciones favorables para que los profesores ensayen nuevas estrategias de enseñanza con acompañamiento técnico y pedagógico continuo. Esto implica promover comunidades de aprendizaje internas, donde los docentes compartan aciertos y dificultades en el uso de recursos multimedia sin temor a sanciones administrativas (Fullan, 2016)."
        ],
        "multimedia_type": "table_leadership",
        "paragraphs_part2": [
            "Para avanzar hacia este modelo en nuestra región, los equipos directivos deben descentralizar decisiones operativas y valorar el liderazgo distribuido entre coordinadores de área y profesores de aula. Cuando las iniciativas que surgen en los departamentos pedagógicos reciben respaldo institucional, los avances metodológicos dejan de ser experiencias aisladas y pasan a consolidarse en la cultura del centro educativo.",
            "Asimismo, la teoría de sistemas enseña que las instituciones escolares no funcionan como entidades cerradas. Su vitalidad depende de su permeabilidad frente a las demandas de las familias, el entorno laboral y los cambios culturales que experimenta el alumnado. La tecnología educativa cobra sentido cuando sirve para tender puentes con la comunidad y facilitar procesos de aprendizaje pertinentes para la vida real de los jóvenes.",
            "En este proceso de cambio institucional, la formación continua del profesorado debe orientarse hacia el desarrollo de competencias tecno-pedagógicas situadas, evitando talleres instrumentales aislados que se limiten a enseñar el funcionamiento técnico de una aplicación. La capacitación docente resulta transformadora cuando abre espacios para reflexionar sobre cómo evaluar formativamente en entornos virtuales, cómo diseñar consignas de trabajo colaborativo y cómo acompañar socioemocionalmente a estudiantes que cursan asignaturas a distancia.",
            "La transformación de un centro escolar depende, en definitiva, de la calidad de sus relaciones humanas y de la capacidad directiva para generar confianza en los equipos docentes. En el contexto de su centro de trabajo, ¿considera que el equipo directivo apoya de forma activa la iniciativa pedagógica de los profesores, o predomina todavía una lógica de fiscalización administrativa que limita la renovación metodológica?"
        ],
        "references": [
            "Bass, B. M., & Avolio, B. J. (1994). <em>Improving organizational effectiveness through transformational leadership</em>. SAGE Publications.",
            "Chiavenato, I. (2014). <em>Introducción a la teoría general de la administración</em> (8.ª ed.). McGraw-Hill.",
            "Fullan, M. (2016). <em>The new meaning of educational change</em> (5th ed.). Teachers College Press.",
            "UNESCO. (2023). <em>Informe de seguimiento de la educación en el mundo: Tecnología en la educación</em>. Ediciones UNESCO."
        ]
    },
    {
        "id": 4,
        "date": "2026-11-03T16:00:00Z",
        "title": "Infraestructura telemática y selección de plataformas para entornos virtuales",
        "tags": ["ArquitecturaEdTech", "SistemasLMS", "Interoperabilidad"],
        "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Armarios de servidores y equipos de red en centro de datos",
        "paragraphs_part1": [
            "En la gestión de proyectos de educación virtual, las decisiones sobre infraestructura técnica suelen delegarse por completo en el personal de sistemas, sin suficiente articulación con los responsables académicos. Esta desconexión suele manifestarse en momentos críticos del calendario escolar: caídas de servidor durante semanas de evaluación, lentitud en la carga de archivos multimedia y dificultades para enlazar la plataforma con el registro de calificaciones.",
            "Cualquier sistema de gestión del aprendizaje (LMS) funciona bajo una arquitectura cliente-servidor distribuida en varias capas: la conectividad externa proveída por los enlaces de telecomunicaciones, los servidores de aplicaciones web y los motores de bases de datos relacionales (Tanenbaum & Wetherall, 2011). Cuando cientos o miles de estudiantes acceden en horarios simultáneos a responder un cuestionario en línea, el consumo de memoria y las peticiones a la base de datos se multiplican con rapidez.",
            "Para un directivo educativo, comprender estos principios elementales es indispensable al momento de planificar el presupuesto institucional. Contratar servicios de hospedaje web compartido sin garantías de concurrencia elástica pone en riesgo la continuidad de las actividades evaluativas. La institución requiere acuerdos de servicio claros, planes de respaldo diario automatizado y protocolos de seguridad informática que protejan la privacidad de los expedientes estudiantiles (Laudon & Laudon, 2020)."
        ],
        "multimedia_type": "diagram_arch",
        "paragraphs_part2": [
            "Otro factor de primer orden en la selección de plataformas es la interoperabilidad técnica. El empleo de estándares abiertos reconocidos internacionalmente, como las especificaciones LTI del consorcio 1EdTech, permite que la institución incorpore simuladores externos, bibliotecas digitales y herramientas de videoconferencia sin quedar atada a un único proveedor comercial privado ni pagar sobrecostos periódicos por licencias de usuario.",
            "La adopción de plataformas de código abierto robustas, como Moodle, respaldadas por servidores bien dimensionados, ha demostrado ser una alternativa económica y técnicamente sostenible para universidades públicas y centros escolares de América Latina. Los recursos ahorrados en licenciamiento privativo pueden reorientarse hacia la capacitación continua del profesorado y el mantenimiento de laboratorios informáticos para los alumnos con mayores carencias de equipamiento.",
            "Asimismo, la gerencia de sistemas educativos debe prever planes de contingencia ante fallos técnicos imprevistos o interrupciones en el suministro eléctrico y de conectividad, situaciones habituales en diversos contextos de nuestra región. Establecer canales de comunicación alternativos, flexibilizar los plazos de entrega de asignaciones cuando se presenten caídas comprobadas del sistema y mantener copias de seguridad accesibles son medidas de gestión indispensables para proteger la tranquilidad de la comunidad académica y garantizar la continuidad formativa, evitando que contingencias técnicas aíslen al alumnado o entorpezcan el desarrollo del calendario académico establecido por las autoridades de la institución educativa.",
            "La estabilidad técnica de un campus virtual no es un asunto secundario de soporte técnico, sino una condición básica para garantizar el derecho a la educación de los estudiantes. Frente a esta necesidad institucional, ¿ha vivido su centro educativo caídas de plataforma en momentos evaluativos clave, y cómo se coordinan actualmente el área técnica y la dirección académica para evitar estos incidentes?"
        ],
        "references": [
            "1EdTech Consortium. (2022). <em>Learning Tools Interoperability (LTI) specification v1.3</em>. 1EdTech.",
            "Laudon, K. C., & Laudon, J. P. (2020). <em>Management information systems: Managing the digital firm</em> (16th ed.). Pearson.",
            "Tanenbaum, A. S., & Wetherall, D. J. (2011). <em>Redes de computadoras</em> (5.ª ed.). Pearson Educación."
        ]
    },
    {
        "id": 5,
        "date": "2026-11-02T14:00:00Z",
        "title": "Analítica de aprendizaje y toma de decisiones basada en datos escolares",
        "tags": ["LearningAnalytics", "GobernanzaDeDatos", "TomaDeDecisiones"],
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Gráficas de datos y métricas en pantalla de ordenador",
        "paragraphs_part1": [
            "Las tasas de deserción en los programas de educación a distancia continúan siendo motivo de preocupación para las instituciones de educación superior en nuestra región. Tradicionalmente, la administración escolar registraba el abandono estudiantil de forma tardía, cuando el alumno ya había dejado de matricularse o figuraba como reprobado en las actas finales del curso (UNESCO, 2023). En los entornos virtuales actuales, sin embargo, el rastro de interacción de los participantes ofrece información valiosa para actuar a tiempo.",
            "La analítica de aprendizaje consiste en la medición, recopilación, análisis y reporte de los datos generados por los estudiantes y sus contextos en las plataformas educativas, con el propósito de comprender y optimizar los procesos formativos (Siemens & Long, 2011). A través del seguimiento de variables como la regularidad de accesos, los tiempos de entrega de asignaciones y la participación en actividades grupales, las coordinaciones académicas pueden identificar patrones de riesgo semanas antes de los exámenes parciales.",
            "Esta información permite estructurar sistemas de alerta temprana orientados a la intervención pedagógica preventiva (Ferguson, 2012). Cuando el sistema identifica a un grupo de estudiantes con desconexión progresiva, los tutores pueden comunicarse de forma proactiva con ellos para indagar dificultades metodológicas o personales, ofreciendo asesorías personalizadas antes de que la desvinculación se convierta en abandono formal."
        ],
        "multimedia_type": "dashboard_analytics",
        "paragraphs_part2": [
            "El valor de estas métricas aumenta cuando los datos se comparten también con los propios estudiantes en forma de paneles de autogestión. Saber cómo marcha el propio ritmo de estudio respecto a los hitos del curso ayuda a que el alumno autorregule sus tiempos de dedicación y tome mayor conciencia de sus hábitos de aprendizaje, favoreciendo la autonomía intelectual en la modalidad virtual.",
            "No obstante, el manejo de datos escolares exige una estricta política ética institucional. Como advierte Daniel (2015), la analítica debe desarrollarse con consentimiento informado, confidencialidad en los registros y criterios claros para que las alertas no deriven en etiquetas negativas que condicionen el trato hacia los estudiantes. La función del algoritmo debe ser orientar el apoyo docente, nunca justificar exclusiones automáticas ni sustituir la relación pedagógica directa.",
            "La interpretación pedagógica de los datos del campus virtual exige que las coordinaciones académicas trabajen de manera conjunta con los docentes tutores. Los reportes estadísticos no deben transformarse en instrumentos de fiscalización laboral sobre el profesorado, sino en insumos compartidos para identificar qué actividades presentan mayor índice de dificultad, qué lecturas generan más dudas y en qué momentos del semestre se hace necesario reforzar las tutorías de apoyo.",
            "La evidencia empírica proporciona claridad para la toma de decisiones directivas, pero su eficacia depende de la sensibilidad con que se utilice en la práctica tutorial. Desde su experiencia institucional, ¿qué medidas de acompañamiento docente consideraría más eficaces para intervenir a tiempo ante alumnos identificados en riesgo, sin hacerlos sentir señalados o vigilados de forma invasiva?"
        ],
        "references": [
            "Daniel, B. (2015). Big Data and analytics in higher education: Opportunities and challenges. <em>British Journal of Educational Technology</em>, 46(5), 904–920.",
            "Ferguson, R. (2012). Learning analytics: Drivers, developments and challenges. <em>International Journal of Technology Enhanced Learning</em>, 4(5-6), 304–317.",
            "Siemens, G., & Long, P. (2011). Penetrating the fog: Analytics in learning and education. <em>EDUCAUSE Review</em>, 46(5), 30–40.",
            "UNESCO. (2023). <em>Tecnología en la educación: ¿Una herramienta en los términos de quién?</em>. Ediciones UNESCO."
        ]
    },
    {
        "id": 6,
        "date": "2026-11-01T12:00:00Z",
        "title": "Gobernanza de la inteligencia artificial y evaluación formativa en el aula",
        "tags": ["InteligenciaArtificial", "EticaEducativa", "PoliticasInstitucionales"],
        "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Representación gráfica de inteligencia artificial y tecnología digital",
        "paragraphs_part1": [
            "La difusión pública de modelos generativos de lenguaje y asistentes de inteligencia artificial ha provocado reacciones encontradas en el ámbito escolar y universitario. Frente al temor de que estas herramientas promuevan el fraude académico o la copia mecánica, varias instituciones optaron inicialmente por prohibir su uso e instalar programas de detección automática en sus campus virtuales. Sin embargo, las directrices internacionales de la UNESCO (2023) subrayan que la prohibición es poco efectiva y que el desafío central consiste en formular políticas de uso responsable centradas en el pensamiento crítico.",
            "Para los equipos directivos, el primer paso implica evitar dos actitudes extremas: rechazar la tecnología como una amenaza que deba erradicarse o aceptarla de manera acrítica sin reflexionar sobre sus sesgos algorítmicos y sus errores de contenido (Holmes et al., 2019). Las herramientas de IA procesan información a partir de patrones lingüísticos previos, lo que exige que los estudiantes desarrollen destrezas de verificación de fuentes y argumentación propia para no depender pasivamente de los resultados automáticos.",
            "En el plano curricular, esta realidad obliga a revisar las formas tradicionales de evaluación. Si una herramienta informática puede resolver un examen memorístico o redactar un resumen descriptivo en pocos segundos, es evidente que el diseño evaluativo ha quedado desfasado respecto a las necesidades formativas actuales. Las asignaturas deben orientarse hacia la evaluación auténtica, mediante actividades que requieran análisis contextualizado, resolución de dilemas éticos y sustentación oral ante docentes y compañeros (Wiggins, 1998)."
        ],
        "multimedia_type": "matrix_ai",
        "paragraphs_part2": [
            "En el ámbito de la gestión institucional, las universidades y colegios necesitan consensuar directrices claras para regular el uso de estas tecnologías. Es recomendable establecer pautas de transparencia que soliciten a los alumnos declarar cuándo y cómo emplearon asistentes de IA en la preparación de sus trabajos, detallando la interacción realizada y la curaduría personal aplicada sobre las respuestas obtenidas.",
            "Asimismo, la institución debe velar por la equidad en el acceso tecnológico, evitando que las suscripciones a herramientas informáticas de pago generen disparidades en el rendimiento académico de los participantes. La formación docente en este campo no debe reducirse al manejo técnico de plataformas, sino incluir debates sobre la privacidad de datos, la autoría intelectual y el uso pedagógico de la tecnología en cada disciplina específica.",
            "En concordancia con las recomendaciones internacionales, las instituciones formativas deben impulsar experiencias de co-diseño donde los estudiantes aprendan a contrastar las respuestas automáticas generadas por modelos de lenguaje con literatura científica arbitrada. La meta pedagógica consiste en formar profesionales capaces de utilizar las herramientas tecnológicas con discernimiento ético, responsabilidad cívica y rigor metodológico en sus respectivas áreas del saber.",
            "La inteligencia artificial plantea preguntas profundas sobre qué significa enseñar y aprender en la sociedad contemporánea. Frente a este panorama institucional, ¿considera usted más conveniente que su centro educativo adopte reglamentos de control disciplinario sobre la IA, o que concentre sus esfuerzos en transformar las rúbricas y estrategias de evaluación docente?"
        ],
        "references": [
            "Holmes, W., Bialik, M., & Fadel, C. (2019). <em>Artificial intelligence in education: Promises and implications for teaching and learning</em>. Center for Curriculum Redesign.",
            "UNESCO. (2023). <em>Guidance for generative AI in education and research</em>. UNESCO Publishing.",
            "Wiggins, G. (1998). <em>Educative assessment: Designing assessments to inform and improve student performance</em>. Jossey-Bass Publishers."
        ]
    },
    {
        "id": 7,
        "date": "2026-10-31T10:00:00Z",
        "title": "Modelos educativos híbridos y sostenibilidad institucional hacia 2030",
        "tags": ["ProspectivaEducativa", "ModelosHibridos", "Educacion2030"],
        "image_url": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Espacio educativo moderno y flexible para trabajo colaborativo",
        "paragraphs_part1": [
            "Al acercarse los plazos fijados por la Agenda 2030 de las Naciones Unidas para el Desarrollo Sostenible, en particular las metas referidas al Objetivo de Desarrollo Sostenible 4 sobre educación de calidad e inclusiva, las instituciones formativas enfrentan la necesidad de repensar su organización física y curricular. Los modelos escolares exclusivamente presenciales o totalmente aislados en la virtualidad dan paso a esquemas flexibles que buscan atender a poblaciones diversas con necesidades cambiantes de formación.",
            "La prospectiva estratégica proporciona herramientas metodológicas para que las directivas escolares no se limiten a reaccionar ante contingencias inmediatas, sino que anticipen escenarios plausibles y diseñen respuestas viables a mediano y largo plazo (Godet, 2007). En este sentido, la consolidación de modelos híbridos sostenibles demanda superar la improvisación logística para construir entornos donde las clases presenciales, los laboratorios prácticos y los espacios virtuales funcionen de manera complementaria y armónica (Gros & García-Peñalvo, 2016).",
            "La sostenibilidad de estos ecosistemas depende también de la soberanía curricular y tecnológica. Las instituciones que sustentan sus programas en Recursos Educativos Abiertos (REA) con licencias Creative Commons reducen de forma significativa los costos de acceso a manuales y materiales didácticos para sus estudiantes, facilitando la democratización del conocimiento y el fortalecimiento de redes de intercambio académico entre instituciones de la región."
        ],
        "multimedia_type": "radar_future",
        "paragraphs_part2": [
            "En el plano operativo, las instituciones deberán considerar criterios de sobriedad digital y eficiencia energética en sus infraestructuras telemáticas. El crecimiento del almacenamiento en la nube y el procesamiento masivo de datos demandan políticas responsables que optimicen los recursos informáticos y promuevan una cultura de cuidado ambiental entre estudiantes y profesores.",
            "La viabilidad de los modelos educativos hacia el año 2030 estará estrechamente vinculada a la capacidad de las instituciones para construir alianzas con la comunidad y el sector productivo local. La tecnología debe ponerse al servicio de problemas reales de cada territorio, permitiendo que la formación académica prepare profesionales comprometidos con el desarrollo social de sus países en lugar de formar graduados desconectados de su realidad social inmediata.",
            "La construcción de estos ecosistemas híbridos hacia el año 2030 demandará directivos comprometidos con la equidad y el acceso abierto al conocimiento. El aprovechamiento de repositorios universitarios compartidos y la producción colaborativa de recursos formativos permitirán abaratar los costos operativos de las instituciones, facilitando que sectores tradicionalmente marginados de la educación superior accedan a programas académicos pertinentes y actualizados, fortaleciendo el tejido social y la democratización del aprendizaje universitario en todas las comunidades de nuestra región.",
            "Los recursos telemáticos cobran su verdadero valor formativo cuando amplían oportunidades de inclusión y dignifican la labor de la comunidad escolar. De cara a los próximos años, ¿cuál considera usted que será la competencia de gestión más determinante que deberán cultivar los directivos educativos para sostener instituciones inclusivas y relevantes en la era digital?"
        ],
        "references": [
            "Godet, M. (2007). <em>Prospectiva estratégica: Para las empresas y los territorios</em>. UNESCO / LIPSOR.",
            "Gros, B., & García-Peñalvo, F. J. (2016). Future trends in the design strategies and technological support of e-learning. En M. Spector (Ed.), <em>The Wiley handbook of learning technology</em> (pp. 264–278). John Wiley & Sons.",
            "UNESCO. (2020). <em>Declaración de Incheon y Marco de Acción para la realización del ODS 4</em>. Ediciones UNESCO."
        ]
    }
]

def render_multimedia(post):
    m_type = post.get("multimedia_type")
    
    if m_type == "audio":
        return '''
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 18px; margin: 24px 0;">
  <p style="font-size: 0.95rem; font-weight: bold; color: #1e293b; margin: 0 0 6px 0;">
    🎙️ Audio Oficial de la Unidad: Fundamentos y Modelos de la Gerencia Educativa
  </p>
  <p style="font-size: 0.85rem; color: #475569; margin: 0 0 14px 0;">
    Ponente: Lic. Emily Leidy Chacón de Romero | Centro Local Anzoátegui — UNA (Duración: 6m 30s)
  </p>
  
  <div style="margin-bottom: 12px;">
    <audio controls preload="metadata" style="width: 100%;">
      <source src="https://anthony-huice.github.io/blog-gerencia-educativa/assets/podcast-educativo.mp3" type="audio/mpeg">
      Su navegador no admite la reproducción de audio HTML5.
    </audio>
  </div>
  
  <div style="font-size: 0.825rem;">
    <a href="https://voca.ro/143LDvk3Ro19" target="_blank" rel="noopener" style="color: #2563eb; text-decoration: underline; font-weight: bold;">
      Enlace directo a Vocaroo (https://voca.ro/143LDvk3Ro19) ↗
    </a>
  </div>
</div>
'''
    elif m_type == "video":
        return '''
<div style="background: #0f172a; border-radius: 8px; overflow: hidden; margin: 24px 0;">
  <div style="background: #1e293b; color: #f8fafc; padding: 10px 14px; font-weight: bold; font-size: 0.9rem;">
    🎥 Ponencia Unidad 2: Comunicación Telemática y Preproducción Audiovisual
  </div>
  <video controls playsinline preload="metadata" style="width: 100%; max-height: 420px; display: block; background: #000;">
    <source src="https://anthony-huice.github.io/blog-gerencia-educativa/assets/video-ponencia-unidad2.mp4" type="video/mp4">
    Su navegador no soporta la reproducción de video HTML5.
  </video>
  <div style="padding: 10px 14px; background: #1e293b; color: #94a3b8; font-size: 0.8rem;">
    Duración: 4m 03s | Grabación de la video-exposición sobre preproducción técnico-pedagógica.
  </div>
</div>
'''
    elif m_type == "table_leadership":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 22px 0;">
  <p style="font-weight: bold; color: #1e293b; font-size: 0.9rem; margin: 0 0 10px 0;">
    Comparación entre el enfoque normativo burocrático y el liderazgo transformacional
  </p>
  <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; color: #334155;">
    <thead>
      <tr style="background: #e2e8f0; text-align: left;">
        <th style="padding: 8px; border: 1px solid #cbd5e1;">Aspecto</th>
        <th style="padding: 8px; border: 1px solid #cbd5e1;">Gestión Normativa Tradicional</th>
        <th style="padding: 8px; border: 1px solid #cbd5e1;">Liderazgo Transformacional</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">Supervisión</td>
        <td style="padding: 8px; border: 1px solid #cbd5e1;">Centrada en el cumplimiento formal y la asistencia.</td>
        <td style="padding: 8px; border: 1px solid #cbd5e1;">Orientada a la facilitación y el respaldo formativo.</td>
      </tr>
      <tr style="background: #f1f5f9;">
        <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">Uso de plataformas</td>
        <td style="padding: 8px; border: 1px solid #cbd5e1;">Manejo del campus como repositorio de documentos.</td>
        <td style="padding: 8px; border: 1px solid #cbd5e1;">Integración del entorno para actividades colaborativas.</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">Innovación docente</td>
        <td style="padding: 8px; border: 1px solid #cbd5e1;">Poco margen para la experimentación pedagógica.</td>
        <td style="padding: 8px; border: 1px solid #cbd5e1;">Promoción de comunidades de práctica entre profesores.</td>
      </tr>
    </tbody>
  </table>
</div>
'''
    elif m_type == "diagram_arch":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 22px 0;">
  <p style="font-weight: bold; color: #1e293b; font-size: 0.9rem; margin: 0 0 10px 0;">
    Capas funcionales de la infraestructura de un campus virtual
  </p>
  <ul style="margin: 0; padding-left: 20px; font-size: 0.85rem; color: #334155; line-height: 1.6;">
    <li><strong>Capa de red y conectividad:</strong> Enlaces redundantes de telecomunicaciones y acuerdos de nivel de servicio (SLA).</li>
    <li><strong>Capa de procesamiento y bases de datos:</strong> Balanceadores de carga y servidores dimensionados para concurrencia masiva.</li>
    <li><strong>Capa de plataforma e integración:</strong> Sistemas LMS compatibles con especificaciones LTI para herramientas externas.</li>
    <li><strong>Capa de seguridad:</strong> Cifrado de comunicaciones mediante protocolos SSL/TLS y copias de seguridad continuas.</li>
  </ul>
</div>
'''
    elif m_type == "dashboard_analytics":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 22px 0;">
  <p style="font-weight: bold; color: #1e293b; font-size: 0.9rem; margin: 0 0 10px 0;">
    Variables habituales en sistemas de alerta temprana para educación en línea
  </p>
  <ul style="margin: 0; padding-left: 20px; font-size: 0.85rem; color: #334155; line-height: 1.6;">
    <li><strong>Frecuencia de acceso al campus:</strong> Registro de días consecutivos de inactividad respecto al promedio del grupo.</li>
    <li><strong>Cumplimiento de tareas iniciales:</strong> Envío de asignaciones diagnósticas durante las primeras tres semanas de curso.</li>
    <li><strong>Participación en foros formativos:</strong> Nivel de interacción con compañeros y docentes en actividades asincrónicas.</li>
    <li><strong>Tiempos de retroalimentación tutorial:</strong> Celeridad con la que el profesorado responde consultas y califica tareas.</li>
  </ul>
</div>
'''
    elif m_type == "matrix_ai":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 22px 0;">
  <p style="font-weight: bold; color: #1e293b; font-size: 0.9rem; margin: 0 0 10px 0;">
    Pautas sugeridas por la UNESCO para el uso de inteligencia artificial en instituciones formativas
  </p>
  <ul style="margin: 0; padding-left: 20px; font-size: 0.85rem; color: #334155; line-height: 1.6;">
    <li><strong>Evaluación formativa y contextualizada:</strong> Priorizar la defensa oral, estudios de caso y argumentación situada frente a exámenes repetitivos.</li>
    <li><strong>Transparencia en el uso de herramientas:</strong> Declaración honesta por parte de los alumnos sobre el empleo de asistentes virtuales en sus textos.</li>
    <li><strong>Equidad en el acceso:</strong> Garantizar que las herramientas recomendadas estén disponibles sin barreras económicas para el alumnado.</li>
    <li><strong>Capacitación docente permanente:</strong> Formar al profesorado en el análisis crítico de sesgos y en el diseño instruccional actualizado.</li>
  </ul>
</div>
'''
    elif m_type == "radar_future":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 22px 0;">
  <p style="font-weight: bold; color: #1e293b; font-size: 0.9rem; margin: 0 0 10px 0;">
    Ejes de sostenibilidad para la educación híbrida hacia el año 2030
  </p>
  <ul style="margin: 0; padding-left: 20px; font-size: 0.85rem; color: #334155; line-height: 1.6;">
    <li><strong>Aulas y entornos flexibles:</strong> Coordinación fluida entre la asistencia presencial y las actividades virtuales estructuradas.</li>
    <li><strong>Recursos Educativos Abiertos (REA):</strong> Utilización de materiales didácticos de dominio público con licencias Creative Commons.</li>
    <li><strong>Eficiencia informática:</strong> Racionalización del almacenamiento en la nube y optimización energética de los centros de datos.</li>
    <li><strong>Vinculación comunitaria:</strong> Orientación de las investigaciones y proyectos escolares hacia las necesidades de cada localidad.</li>
  </ul>
</div>
'''
    return ""

def generate_entry_body(post):
    multimedia_html = render_multimedia(post)
    ref_items = "".join([f"<li style='margin-bottom: 6px; padding-left: 1.5rem; text-indent: -1.5rem;'>{r}</li>" for r in post["references"]])
    
    p_part1 = "".join([f"<p style='margin-bottom: 16px;'>{p}</p>" for p in post["paragraphs_part1"]])
    p_part2 = "".join([f"<p style='margin-bottom: 16px;'>{p}</p>" for p in post["paragraphs_part2"]])
    
    html = f'''
<!-- Fotografía de contextualización -->
<div style="margin-bottom: 22px; border-radius: 8px; overflow: hidden;">
  <img src="{post['image_url']}" alt="{post['image_alt']}" style="width: 100%; height: auto; max-height: 420px; object-fit: cover; display: block;">
</div>

<!-- Texto de apertura y contextualización directa (sin rótulos artificiales) -->
<div style="font-size: 1.025rem; line-height: 1.75; color: #1e293b; text-align: justify;">
  {p_part1}
  
  {multimedia_html}
  
  {p_part2}
</div>

<!-- Referencias bibliográficas formales APA 7 -->
<div style="margin-top: 25px; padding-top: 15px; border-top: 1px dashed #cbd5e1; font-size: 0.825rem; color: #475569; font-family: sans-serif;">
  <strong style="text-transform: uppercase; color: #1e293b; display: block; margin-bottom: 8px; letter-spacing: 0.03em;">
    Referencias Bibliográficas (Normas APA 7.ª Edición)
  </strong>
  <ul style="list-style: none; padding-left: 0; line-height: 1.55; margin: 0;">
    {ref_items}
  </ul>
</div>
'''
    return html

def main():
    out_dir = "/home/anthony/Escritorio/pdvsa 2/blogger_entradas"
    os.makedirs(out_dir, exist_ok=True)
    
    print("--- AUDITORÍA Y HUMANIZACIÓN DE ENTRADAS ---")
    for post in POSTS:
        i = post["id"]
        title = post["title"]
        tags_str = ", ".join(post["tags"])
        body = generate_entry_body(post)
        
        clean_text = re.sub(r'<[^>]+>', ' ', body)
        words = re.findall(r'\b\w+\b', clean_text)
        print(f"Entrada {i} [{post['date'][:10]}]: {len(words)} palabras | Tags ({len(post['tags'])}): {tags_str}")
        
        filename = f"Entrada_{i}_{post['tags'][0]}.html"
        filepath = os.path.join(out_dir, filename)
        
        content = f'''<!-- 
================================================================================
ENTRADA #{i} HUMANIZADA PARA BLOGGER
TITULO: {title}
ETIQUETAS EXACTAS: {tags_str}
================================================================================
-->

<div style="font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.7; color: #1e293b; max-width: 820px; margin: 0 auto;">
{body}
</div>
'''
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # Master XML import file
    entries_xml = []
    for post in POSTS:
        i = post["id"]
        title = post["title"]
        date_str = post["date"]
        body = generate_entry_body(post)
        wrapper = f'<div style="font-family: system-ui, -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif; line-height: 1.7; color: #1e293b; max-width: 820px; margin: 0 auto;">{body}</div>'
        
        categories = ['<category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/blogger/2008/kind#post"/>']
        for t in post["tags"]:
            categories.append(f'<category scheme="http://www.blogger.com/atom/ns#" term="{t}"/>')
        cat_xml = "\n    ".join(categories)
        
        entry_str = f'''  <entry>
    <id>tag:blogger.com,1999:blog-1000000000.post-{i}</id>
    <published>{date_str}</published>
    <updated>{date_str}</updated>
    {cat_xml}
    <title type="text">{title}</title>
    <content type="html"><![CDATA[{wrapper}]]></content>
    <author>
      <name>Anthony Huice</name>
      <uri>https://anthony-huice.github.io/blog-gerencia-educativa/</uri>
    </author>
  </entry>'''
        entries_xml.append(entry_str)

    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/" xmlns:georss="http://www.georss.org/georss" xmlns:gd="http://schemas.google.com/g/2005" xmlns:thr="http://purl.org/syndication/thread/1.0">
  <id>tag:blogger.com,1999:blog-1000000000</id>
  <updated>2026-11-06T23:59:00Z</updated>
  <title type="text">TecnoGerencia Educativa: Liderazgo y Sistemas Digitales</title>
  <subtitle type="html">Bitácora académica sobre liderazgo directivo, arquitecturas telemáticas, analítica de aprendizaje y prospectiva en entornos virtuales.</subtitle>
  <author>
    <name>Anthony Huice</name>
    <uri>https://anthony-huice.github.io/blog-gerencia-educativa/</uri>
    <email>anthonyhuice@gmail.com</email>
  </author>
{chr(10).join(entries_xml)}
</feed>'''

    xml_path = os.path.join(out_dir, "blogger_import.xml")
    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"\n¡Éxito! Archivo maestro humanizado exportado en: {xml_path}")

if __name__ == "__main__":
    main()
