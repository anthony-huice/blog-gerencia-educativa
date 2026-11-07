# -*- coding: utf-8 -*-
"""
Script generador del Blog Educativo Optimizado
Gerencia de Sistemas Educativos basados en Tecnología
7 Entradas, Audio en Entrada 1 (Principal), Extensión precisa (620-720 palabras),
Imágenes referenciales reales de alta resolución y normas APA 7.
"""

import os
import re

POSTS = [
    {
        "id": 1,
        "is_flagship": True,
        "date": "2026-11-06T23:59:00Z",
        "title": "La voz del cambio institucional: Fundamentos epistemológicos y liderazgo situacional en la gerencia pedagógica moderna",
        "tags": ["GerenciaEducativa", "PodcastPedagogico", "LiderazgoSituacional"],
        "image_url": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Micrófono profesional de condensador en estudio de grabación de podcast educativo",
        "image_caption": "Figura 1. La producción sonora como mediador pedagógico y catalizador del debate directivo.",
        "metaphor_title": "El Timonel Situacional en Altamar",
        "metaphor_caption": "Las corrientes del cambio educativo no admiten capitanes rígidos; el gerente debe calibrar su timón situacional para responder a la incertidumbre sin desviar el rumbo formativo.",
        "context_trigger": "En el marco de la cuarta unidad formativa, inauguramos este espacio con la difusión y análisis del podcast académico oficial conducido por la investigadora <strong>Lic. Emily Leidy Chacón de Romero</strong> (Centro Local Anzoátegui, Universidad Nacional Abierta). El detonante del debate surge de una paradoja recurrente: ¿por qué los modelos de administración mercantil fracasan sistemáticamente al trasplantarse a instituciones escolares sin una previa reconversión humanista y pedagógica?",
        "analysis_paragraphs": [
            "Como expone con rigor la Lic. Chacón de Romero en su disertación sonora, la función gerencial general se define clásicamente como la coordinación, dirección y optimización de recursos humanos, materiales y tecnológicos para maximizar la eficiencia en los procesos de <em>Planificación, Organización, Dirección y Control</em> (Chiavenato, 2014). Sin embargo, la <strong>gerencia educativa encierra una teleología diametralmente opuesta al ámbito corporativo mercantil</strong>: su fin no es la rentabilidad financiera ni la acumulación de plusvalía, sino la <strong>transformación social, la equidad ciudadana y la emancipación integral del ser humano</strong>.",
            "Esta diferenciación ontológica descansa sobre cuatro fundamentos interdisciplinarios articulados en el audio: la <em>teoría clásica y orgánica</em>, que provee orden, estructura y delimitación clara de roles institucionales; la <em>teoría humanista</em>, que sitúa en el núcleo la salud del clima escolar, la empatía y la motivación docente; la <em>teoría general de sistemas</em>, que concibe a la escuela como un ecosistema abierto, dinámico y permeable frente a la comunidad; y el <em>fundamento socio-pedagógico</em>, que supedita toda decisión técnica y administrativa al desarrollo ético de los estudiantes (Fullan, 2016; UPEL, 2016).",
            "Un aporte medular del podcast es la caracterización de los siete modelos gerenciales coexistentes: el normativo (previsión y rigidez), el prospectivo (diseño de escenarios futuros), el estratégico (análisis FODA), el estratégico-situacional (negociación y viabilidad política), el de calidad total (satisfacción de procesos), el de reingeniería (ruptura de paradigmas ante crisis severas) y el comunicacional (redes de compromisos compartidos). Como concluye la expositora, el directivo escolar del siglo XXI no puede atrincherarse en un único dogma burocrático; debe consolidarse como un <strong>líder situacional e integrador</strong> (Hersey & Blanchard, 1988), capaz de modular su estilo de conducción según la madurez tecno-pedagógica de su equipo.",
            "En los ecosistemas mediados por plataformas digitales, esta flexibilidad resulta decisiva. El gestor educativo no fiscaliza horarios estáticos; facilita condiciones para el co-diseño colaborativo, la innovación curricular y el acompañamiento afectivo de la comunidad escolar."
        ],
        "multimedia_type": "audio",
        "discussion_question": "¿Considera usted que en nuestras instituciones educativas prevalece aún el modelo normativo burocrático, o se evidencia una transición real hacia el liderazgo situacional y comunicacional? ¿Cuál es el principal freno estructural que impide dicha evolución?",
        "references": [
            "Chacón de Romero, E. L. (2026). <em>Aspectos fundamentales de la gerencia educativa: De las bases teóricas al liderazgo situacional</em> [Episodio de podcast de audio]. Vocaroo. <a href=\"https://voca.ro/1i8rKfimqgjM\" target=\"_blank\" rel=\"noopener\">https://voca.ro/1i8rKfimqgjM</a>",
            "Chiavenato, I. (2014). <em>Comportamiento organizacional: La dinámica del éxito en las organizaciones</em> (3.ª ed.). McGraw-Hill Educación.",
            "Fullan, M. (2016). <em>The new meaning of educational change</em> (5th ed.). Teachers College Press.",
            "Hersey, P., & Blanchard, K. H. (1988). <em>Management of organizational behavior: Utilizing human resources</em> (5th ed.). Prentice-Hall.",
            "Universidad Pedagógica Experimental Libertador [UPEL]. (2016). <em>Manual de trabajos de grado de especialización y maestría y tesis doctorales</em> (5.ª ed.). FEDUPEL."
        ]
    },
    {
        "id": 2,
        "is_flagship": False,
        "date": "2026-11-05T20:00:00Z",
        "title": "Más allá de la pantalla fría: Presencia cognitiva, sincronía y el arte de articular el blended learning",
        "tags": ["ComunicacionDigital", "PresenciaCognitiva", "AprendizajeMezclado"],
        "image_url": "https://images.unsplash.com/photo-1588196749597-9ff075ee6b5b?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Estudiante interactuando en sesión telemática de videoconferencia y plataforma virtual",
        "image_caption": "Figura 2. La comunicación telemática como puente relacional y dialógico en la educación a distancia.",
        "metaphor_title": "Los Puentes Invisibles de la Telemática",
        "metaphor_caption": "La virtualidad no separa a los actores educativos; transmuta la lejanía física en proximidad afectiva y dialógica mediante la sabia orquestación de canales síncronos y asíncronos.",
        "context_trigger": "Como complemento y síntesis de la ponencia desarrollada en la <strong>Unidad 2 de nuestro programa</strong>, este artículo examina el circuito comunicativo digital. El detonante de la investigación fue la crisis de fatiga de pantalla y deserción escolar provocada por la transposición acrítica de clases magistrales a salas de videoconferencia, confundiendo la mera conectividad con la presencia pedagógica significativa.",
        "analysis_paragraphs": [
            "En la gestión tecno-pedagógica de la educación a distancia, es fundamental comprender que los <strong>canales síncronos (videoconferencias WebRTC, chats en vivo)</strong> y los <strong>canales asíncronos (foros reflexivos, correos institucionales, repositorios anotados)</strong> cumplen funciones cognitivas complementarias pero de naturaleza radicalmente distinta (Garrison et al., 2000).",
            "La sincronía aporta calidez humana, fomenta la <em>presencia social inmediata</em> y resuelve dudas operativas complejas en tiempo real; no obstante, su abuso impone rigidez temporal y amplía la brecha de exclusión para aquellos estudiantes con conectividad deficiente o planes de datos restringidos. Por su parte, la asincronía constituye el verdadero laboratorio del pensamiento crítico superior, pues brinda el tiempo necesario para la lectura pausada, la contrastación de fuentes y la redacción autorregulada sin presiones temporales externas (Moore, 1993).",
            "La articulación armónica de ambos mundos se materializa en el <strong>aprendizaje mezclado o blended learning</strong>. Lejos de representar un compromiso logístico superficial, el modelo híbrido redefine la economía temporal del aula. Bajo esquemas de aula invertida (<em>flipped classroom</em>), el tiempo síncrono se reserva exclusivamente para la deliberación dialéctica, el aprendizaje basado en dilemas y el trabajo en talleres colaborativos, mientras que los contenidos basales se asimilan asincrónicamente mediante guiones didácticos estructurados (Bates, 2019).",
            "Asimismo, la teoría de la distancia transaccional de Moore demuestra que la separación no es geográfica, sino pedagógica y psicológica: una clase presencial expositiva puede encerrar una distancia transaccional enorme si no existe diálogo, mientras que un entorno virtual interactivo bien moderado genera cercanía afectiva y resonancia intelectual inmediata.",
            "La integración estratégica del modelo blended learning exige una profunda reconceptualización del rol docente: el profesor transita de ser un mero expositor magistral a convertirse en un curador de contenidos, diseñador de experiencias dialógicas y facilitador de la inteligencia colectiva. Este tránsito demanda de la gerencia institucional programas sistemáticos de acompañamiento tecno-pedagógico que capaciten al profesorado en el dominio de dinámicas interactivas, rúbricas de evaluación formativa y gestión empática de la presencia socioemocional a través de la pantalla.",
            "El gerente educativo no puede permitir la improvisación en el diseño instruccional: la elección de un canal tecnológico es una decisión estratégica y política que condiciona la inclusión social y la profundidad formativa de los aprendizajes universitarios."
        ],
        "multimedia_type": "video",
        "discussion_question": "¿Cómo equilibra su institución los espacios síncronos y asíncronos para evitar la saturación cognitiva del alumnado sin sacrificar la sensación de acompañamiento docente?",
        "references": [
            "Bates, A. W. (2019). <em>Teaching in a digital age: Guidelines for designing teaching and learning</em> (2nd ed.). Tony Bates Associates Ltd.",
            "Garrison, D. R., Anderson, T., & Archer, W. (2000). Critical inquiry in a text-based environment: Computer conferencing in higher education. <em>The Internet and Higher Education</em>, 2(2-3), 87–105.",
            "Moore, M. G. (1993). Theory of transactional distance. En D. Keegan (Ed.), <em>Theoretical principles of distance education</em> (pp. 22–38). Routledge.",
            "Universidad Pedagógica Experimental Libertador [UPEL]. (2016). <em>Manual de trabajos de grado</em>. FEDUPEL."
        ]
    },
    {
        "id": 3,
        "is_flagship": False,
        "date": "2026-11-04T18:00:00Z",
        "title": "¿Gestionar la rutina o liderar la incertidumbre? El giro copernicano del directivo escolar ante la disrupción telemática",
        "tags": ["LiderazgoEducativo", "TransformacionDigital", "GestionEscolar"],
        "image_url": "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Equipo directivo y académico debatiendo estrategias pedagógicas innovadoras",
        "image_caption": "Figura 3. El liderazgo transformacional como motor de la cultura digital comunitaria.",
        "metaphor_title": "El Director de Orquesta Telemática",
        "metaphor_caption": "El líder educativo no interpreta cada instrumento de forma aislada; armoniza voluntades y disipa temores para que la técnica jamás opaque la melodía de la enseñanza.",
        "context_trigger": "Informes recientes de la UNESCO (2023) constatan que más del 65% de los proyectos de modernización tecnológica escolar en América Latina fracasan no por obsolescencia técnica de los equipos, sino por la resistencia cultural y el apego directivo a esquemas burocráticos rígidos que ahogan la iniciativa pedagógica.",
        "analysis_paragraphs": [
            "El <strong>modelo burocrático-normativo clásico</strong> concebía al director como un mero auditor de reglamentos, firmas y asistencia física. Sin embargo, en un entorno telemático caracterizado por redes distribuidas y saberes descentralizados, este enfoque punitivo resulta estéril. Como afirman Bass y Avolio (1994), la institución moderna exige un <strong>liderazgo transformacional</strong> fundamentado en la inspiración, la estimulación intelectual y el acompañamiento empático de cada miembro del cuerpo docente.",
            "El directivo contemporáneo no debe imponer herramientas digitales por decreto administrativo; su labor consiste en propiciar comunidades de práctica donde los educadores experimenten metodologías emergentes sin temor al error técnico. La tecnología debe concebirse como un territorio de emancipación formativa, no como una carga fiscalizadora adicional que sobrecargue la jornada laboral docente (Fullan, 2016).",
            "Esta transformación demanda un rediseño de la cultura organizacional. En lugar de una estructura piramidal hermética, la escuela conectada opera como una red orgánica orientada al aprendizaje mutuo. Como postula Chiavenato (2014), la eficacia de los sistemas abiertos radica en su capacidad de retroalimentación constante con el medio social y familiar que los rodea.",
            "La meta superior de la gerencia escolar es afianzar una cultura institucional abierta al aprendizaje permanente. Cuando el equipo directivo lidera con el ejemplo, participando en foros virtuales y valorando la creatividad metodológica, la institución entera se convierte en un sistema resiliente capaz de navegar los cambios tecnológicos con pertinencia y dignidad.",
            "Para la gerencia educativa en América Latina, el reto primordial consiste en trascender la retórica de la modernización cosmética para asumir la cultura digital como una verdadera práctica democrática y participativa. Esto implica descentralizar la toma de decisiones, fomentar el liderazgo distribuido entre coordinadores y docentes, y reconocer las iniciativas locales de innovación que nacen en las cátedras, convirtiendo los aciertos pedagógicos individuales en patrimonio compartido de toda la comunidad escolar.",
            "En concordancia con los postulados de la teoría general de sistemas, la institución educativa que abraza el liderazgo transformacional no opera como una isla aislada; articula sinergias permanentes con el entorno socio-comunitario, transformando el campus virtual en un espacio de diálogo abierto y democratización del conocimiento y el fortalecimiento del compromiso cívico en la sociedad en red.",
            "En última instancia, transformar una escuela no consiste en saturarla de dispositivos electrónicos, sino en resignificar las relaciones humanas mediadas por la tecnología para ponerlas al servicio de la formación integral de los estudiantes."
        ],
        "multimedia_type": "table_leadership",
        "discussion_question": "¿Actúa el equipo directivo de su institución como un facilitador transformador de la innovación tecno-pedagógica o persiste un control normativo burocrático que frena el cambio?",
        "references": [
            "Bass, B. M., & Avolio, B. J. (1994). <em>Improving organizational effectiveness through transformational leadership</em>. SAGE Publications.",
            "Chiavenato, I. (2014). <em>Introducción a la teoría general de la administración</em> (8.ª ed.). McGraw-Hill.",
            "Fullan, M. (2016). <em>The new meaning of educational change</em> (5th ed.). Teachers College Press.",
            "UNESCO. (2023). <em>Informe de seguimiento de la educación en el mundo: Tecnología en la educación</em>. Ediciones UNESCO."
        ]
    },
    {
        "id": 4,
        "is_flagship": False,
        "date": "2026-11-03T16:00:00Z",
        "title": "Los cimientos invisibles del aula virtual: Por qué la pedagogía digital fracasa si la arquitectura telemática colapsa",
        "tags": ["ArquitecturaEdTech", "SistemasLMS", "Interoperabilidad"],
        "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Racks de servidores e infraestructura de red para centros de datos educativos",
        "image_caption": "Figura 4. Infraestructura de servidores y conectividad de alta disponibilidad en campus virtuales.",
        "metaphor_title": "Los Cimientos de la Catedral Invisible",
        "metaphor_caption": "El discurso pedagógico más avanzado se desmorona en un segundo si los servidores colapsan y la red no responde ante la concurrencia masiva de la comunidad estudiantil.",
        "context_trigger": "Cada cierre de semestre universitario se repite el mismo drama telemático: la plataforma institucional colapsa por saturación de concurrencia durante la entrega de evaluaciones clave. Esta avería no es un imprevisto técnico inevitable, sino el síntoma de una gestión directiva que desvincula la planificación académica de la auditoría de infraestructura.",
        "analysis_paragraphs": [
            "Todo entorno virtual de aprendizaje reposa sobre una <strong>arquitectura Cliente-Servidor distribuida de múltiples capas</strong> (Tanenbaum & Wetherall, 2011). Cada clic estudiantil desencadena peticiones HTTP/HTTPS que atraviesan balanceadores de carga, servidores de aplicaciones y consultas intensivas a bases de datos relacionales.",
            "Si la gerencia educativa no audita los acuerdos de nivel de servicio (SLA), el ancho de banda y la capacidad elástica en la nube, condena a sus docentes y alumnos a la frustración y a la interrupción del derecho al aprendizaje. La soberanía tecnológica exige, además, apostar por <strong>estándares abiertos de interoperabilidad (LTI de 1EdTech)</strong> que eviten el secuestro por proveedores comerciales cautivos (Laudon & Laudon, 2020).",
            "Asimismo, la seguridad perimetral de la información institucional representa un deber ineludible. El manejo de registros confidenciales, calificaciones y datos personales de los estudiantes demanda protocolos estrictos de cifrado SSL/TLS, cortafuegos de aplicaciones web y respaldos automatizados continuos para evitar pérdidas irreparables ante fallos de hardware o ciberataques.",
            "La gestión directiva de sistemas tecnológicos requiere líderes bilingües: capaces de dialogar con el vicerrector pedagógico para traducir las metas curriculares en especificaciones de concurrencia, y al mismo tiempo capaces de fiscalizar al equipo de redes para asegurar planes de redundancia, respaldos automatizados diarios y planes de recuperación ante desastres.",
            "Asimismo, la gerencia de infraestructura debe contemplar la sostenibilidad operativa y financiera mediante acuerdos claros de gobernanza telemática. La adquisición de software propietario costoso suele drenar los presupuestos educativos; por el contrario, la implementación de ecosistemas de código abierto robustos (como Moodle) respaldados por una infraestructura de servidores escalable permite reinvertir los recursos económicos en la formación continua del talento humano y en el equipamiento de laboratorios para los estudiantes.",
            "La elección de la infraestructura telemática debe responder a criterios de escalabilidad elástica y tolerancia a fallos. Un centro educativo no puede depender de soluciones improvisadas de alojamiento compartido que colapsen ante picos de concurrencia; requiere servidores dedicados o instancias en la nube optimizadas para soportar el tráfico simultáneo de miles de estudiantes durante períodos de evaluación intensiva, garantizando la equidad en el acceso.",
            "La robustez telemática de una escuela es, en esencia, la salvaguarda material de la continuidad pedagógica y la tranquilidad de su comunidad educativa."
        ],
        "multimedia_type": "diagram_arch",
        "discussion_question": "¿Ha sufrido su centro escolar caídas de plataforma en momentos evaluativos críticos? ¿Cómo justificaría ante la directiva la inversión en servidores como una garantía pedagógica?",
        "references": [
            "1EdTech Consortium. (2022). <em>Learning Tools Interoperability (LTI) specification v1.3</em>. 1EdTech.",
            "Laudon, K. C., & Laudon, J. P. (2020). <em>Management information systems: Managing the digital firm</em> (16th ed.). Pearson.",
            "Tanenbaum, A. S., & Wetherall, D. J. (2011). <em>Redes de computadoras</em> (5.ª ed.). Pearson Educación."
        ]
    },
    {
        "id": 5,
        "is_flagship": False,
        "date": "2026-11-02T14:00:00Z",
        "title": "El algoritmo como aliado pedagógico: Cómo la analítica de aprendizaje rescata trayectorias escolares antes de la deserción",
        "tags": ["LearningAnalytics", "GobernanzaDeDatos", "TomaDeDecisiones"],
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Gráficas de datos analíticos y métricas de rendimiento en pantalla digital",
        "image_caption": "Figura 5. Métricas de interacción y sistemas de alerta temprana para prevenir la deserción escolar.",
        "metaphor_title": "El Radar Meteorológico de la Escuela",
        "metaphor_caption": "Los datos telemáticos no son cifras frías: son la cartografía térmica que avisa a tiempo de las turbulencias académicas para extender la mano antes del abandono.",
        "context_trigger": "En la educación a distancia latinoamericana, los índices de abandono temprano oscilan entre el 35% y el 50% durante el primer año formativo (UNESCO, 2023). Tradicionalmente, la escuela reaccionaba de forma tardía, cuando el alumno ya había desertado; hoy, los datos del campus virtual permiten prever el riesgo semanas antes de que ocurra.",
        "analysis_paragraphs": [
            "La <strong>analítica del aprendizaje (Learning Analytics)</strong> consiste en la medición, recopilación y modelado de las huellas digitales que dejan los estudiantes al interactuar con el entorno virtual, con el propósito expreso de optimizar los procesos formativos y los entornos donde se desarrollan (Siemens & Long, 2011).",
            "Para el equipo directivo, estas métricas permiten estructurar <em>Sistemas de Alerta Temprana (Early Warning Systems)</em>. Si los algoritmos detectan que un estudiante reduce drásticamente su frecuencia de ingreso o no interactúa en los foros iniciales, la institución activa tutorías personalizadas y apoyos socioemocionales inmediatos, sustituyendo la sanción por la prevención afectiva (Ferguson, 2012).",
            "De este modo, la toma de decisiones directiva abandona la mera intuición empírica para fundamentarse en evidencias objetivas de aprendizaje. El monitoreo en tiempo real de los tiempos de retroalimentación docente y de los patrones de entrega de tareas permite identificar cuellos de botella curriculares y ajustar las cargas instruccionales antes de que provoquen el colapso cognitivo del grupo.",
            "No obstante, esta telemetría plantea desafíos éticos capitales: los datos deben gestionarse bajo estrictas políticas de confidencialidad, consentimiento informado y protección de la privacidad, evitando a toda costa la creación de perfiles estigmatizantes basados en sesgos algorítmicos automáticos (Daniel, 2015).",
            "El impacto de la analítica del aprendizaje se potencia sustancialmente cuando los datos se devuelven de manera formativa a los propios estudiantes. La habilitación de paneles de autogestión donde el aprendiz visualiza su propio ritmo de progreso, sus tiempos de estudio y sus áreas de oportunidad estimula la autorregulación metacognitiva y la responsabilidad personal sobre su trayectoria académica, superando la visión fiscalizadora del control administrativo.",
            "La efectividad de la analítica educativa descansa en la celeridad con que la institución convierte los datos en intervenciones pedagógicas oportunas. La detección precoz de estudiantes desvinculados permite activar protocolos de acompañamiento personalizado y tutorías entre pares, logrando revertir trayectorias de abandono antes de que se consoliden como deserciones definitivas en las estadísticas oficiales del plantel.",
            "La analítica nunca sustituye la mirada cálida del educador; es una potente linterna que ilumina las zonas de sombra para garantizar que ningún estudiante quede atrás en el silencio de la red."
        ],
        "multimedia_type": "dashboard_analytics",
        "discussion_question": "Si su institución contara con alertas tempranas de deserción, ¿qué acciones de tutoría priorizaría para apoyar al estudiante sin hacerlo sentir etiquetado negativamente?",
        "references": [
            "Daniel, B. (2015). Big Data and analytics in higher education: Opportunities and challenges. <em>British Journal of Educational Technology</em>, 46(5), 904–920.",
            "Ferguson, R. (2012). Learning analytics: Drivers, developments and challenges. <em>International Journal of Technology Enhanced Learning</em>, 4(5-6), 304–317.",
            "Siemens, G., & Long, P. (2011). Penetrating the fog: Analytics in learning and education. <em>EDUCAUSE Review</em>, 46(5), 30–40.",
            "UNESCO. (2023). <em>Tecnología en la educación: ¿Una herramienta en los términos de quién?</em>. Ediciones UNESCO."
        ]
    },
    {
        "id": 6,
        "is_flagship": False,
        "date": "2026-11-01T12:00:00Z",
        "title": "Inteligencia artificial en el consejo directivo: Políticas institucionales, integridad académica y la brújula ética de la escuela",
        "tags": ["InteligenciaArtificial", "EticaEducativa", "PoliticasInstitucionales"],
        "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Representación abstracta y conceptual de la inteligencia artificial y redes neuronales",
        "image_caption": "Figura 6. El dilema ético y pedagógico de la gobernanza de la inteligencia artificial en la escuela.",
        "metaphor_title": "El Fuego de Prometeo en el Claustro",
        "metaphor_caption": "La Inteligencia Artificial es un fuego potente que puede iluminar el juicio crítico o consumir la integridad formativa; el directivo no debe prohibirlo por pánico, sino forjar el crisol ético para conducirlo con sabiduría.",
        "context_trigger": "Ante la irrupción de los modelos generativos de lenguaje, muchas instituciones escolares reaccionaron prohibiendo su acceso e instalando detectores automáticos de plagio. No obstante, la UNESCO (2023) sentenció con claridad: la prohibición es inviable e ineficaz; las escuelas requieren marcos de gobernanza que enseñen a pensar críticamente *junto* a la inteligencia artificial.",
        "analysis_paragraphs": [
            "El liderazgo educativo debe sortear dos trampas cognitivas: la <strong>tecnofobia punitiva</strong> (que niega la realidad tecnológica y pretende evaluar como en el siglo XIX) y la <strong>tecnofilia acrítica</strong> (que cede el pensamiento reflexivo a la máquina sin cuestionar sus sesgos algorítmicos ni sus alucinaciones factuales) (Holmes et al., 2019).",
            "La adopción directiva de la IA exige una reforma profunda hacia la <strong>evaluación auténtica</strong> (Wiggins, 1998). Si un modelo lingüístico aprueba con facilidad un examen de contenidos memorísticos, lo que ha colapsado es la concepción tradicional de evaluación escolar. Las instituciones deben priorizar el razonamiento situado, la resolución de dilemas éticos reales y la argumentación oral defendida frente a pares.",
            "Desde la perspectiva de la gestión estratégica, las universidades y centros escolares deben emitir códigos de conducta basados en la pedagogía del co-diseño: el estudiante aprende a dialogar críticamente con la IA, a verificar rigurosamente la veracidad de las fuentes citadas y a explicitar el grado de contribución algorítmica en sus producciones.",
            "La gobernanza institucional debe plasmarse en directrices claras: transparencia en la declaración de prompts, equidad en el acceso a herramientas sin desventajas socioeconómicas y programas permanentes de alfabetización informacional crítica para docentes y estudiantes.",
            "El desafío ético de la inteligencia artificial convoca a los equipos directivos a reflexionar sobre la preservación de la autoría y la singularidad de la voz estudiantil. La política institucional no debe centrarse en la cacería de textos sintéticos mediante detectores falibles, sino en inspirar a los alumnos a formular argumentos originales, situados en su contexto comunitario, donde la inteligencia artificial funcione como un interlocutor provocador pero nunca como un reemplazo de la conciencia reflexiva.",
            "En este marco, las instituciones escolares deben promover una alfabetización algorítmica integral que trascienda el mero uso instrumental. Formar a los futuros profesionales exige capacitarlos para evaluar críticamente las respuestas de los modelos de lenguaje, identificar sesgos culturales o de género y comprender las implicaciones ecológicas y de privacidad asociadas al procesamiento de datos masivos.",
            "La inteligencia artificial debe permanecer siempre como un andamio cognitivo subordinado al juicio moral y a la creatividad ética del ser humano."
        ],
        "multimedia_type": "matrix_ai",
        "discussion_question": "¿Debe la gerencia educativa regular la Inteligencia Artificial mediante códigos sancionatorios o mediante el rediseño de rúbricas hacia la evaluación auténtica?",
        "references": [
            "Holmes, W., Bialik, M., & Fadel, C. (2019). <em>Artificial intelligence in education: Promises and implications for teaching and learning</em>. Center for Curriculum Redesign.",
            "UNESCO. (2023). <em>Guidance for generative AI in education and research</em>. UNESCO Publishing.",
            "Wiggins, G. (1998). <em>Educative assessment: Designing assessments to inform and improve student performance</em>. Jossey-Bass Publishers."
        ]
    },
    {
        "id": 7,
        "is_flagship": False,
        "date": "2026-10-31T10:00:00Z",
        "title": "La escuela expandida hacia el 2030: Sostenibilidad, ubicuidad y el renacimiento del pacto socioeducativo",
        "tags": ["ProspectivaEducativa", "ModelosHibridos", "Educacion2030"],
        "image_url": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1000&q=80",
        "image_alt": "Espacio educativo moderno, colaborativo, flexible y mediado por tecnologías",
        "image_caption": "Figura 7. Ecosistemas de aprendizaje expandidos y sostenibles al horizonte 2030.",
        "metaphor_title": "El Árbol Biónico del Ecosistema Escolar",
        "metaphor_caption": "Las raíces institucionales deben nutrirse de la vocación humanista comunitaria, mientras sus ramas digitales se proyectan al horizonte de la educación ubicua y sostenible.",
        "context_trigger": "En el camino decisivo hacia el cumplimiento del Objetivo de Desarrollo Sostenible 4 (ODS 4: Educación de Calidad, Equitativa e Inclusiva), la institución escolar física ha dejado de monopolizar el acceso a la cultura letrada. La gestión directiva prospectiva es indispensable para mantener vivas y pertinentes nuestras instituciones en un entorno de continua metamorfosis.",
        "analysis_paragraphs": [
            "Como postulaba Godet (2007), el futuro no se padece pasivamente: se diseña y se construye mediante la <strong>prospectiva estratégica</strong>. En la gerencia escolar contemporánea, esto implica anticipar escenarios de crisis y formular modelos de <em>ecosistemas híbridos de aprendizaje</em> que trasciendan las cuatro paredes del aula tradicional (Gros & García-Peñalvo, 2016).",
            "Hacia el 2030, las escuelas sostenibles serán aquellas que articulen armónicamente microcredenciales verificables, repositorios de Recursos Educativos Abiertos (REA) con licenciamiento Creative Commons y políticas de sobriedad energética digital que reduzcan la huella ecológica de la computación en la nube.",
            "La convergencia entre la inteligencia colectiva y las tecnologías emergentes exige directivos con una sólida sensibilidad social, capaces de liderar instituciones que garanticen la inclusión efectiva de sectores históricamente desfavorecidos mediante redes de conectividad comunitaria y contenidos hiperlocales pertinentes.",
            "La infraestructura tecnológica jamás debe erigirse como un fin en sí misma; es el medio para democratizar el saber y reparar las deudas históricas de exclusión territorial que han afectado a nuestras comunidades en Venezuela y América Latina.",
            "Hacia el año 2030, la educación universitaria y media requerirá un nuevo pacto entre la tecnología y la ciudadanía. Los rectores y directores escolares deberán cultivar una visión humanista inquebrantable para asegurar que la digitalización no ensanche las brechas de desigualdad, sino que actúe como un vehículo de inclusión social, permitiendo que poblaciones rurales y sectores vulnerables accedan a formación de excelencia internacional sin abandonar sus territorios.",
            "La sostenibilidad de los modelos educativos hacia el año 2030 dependerá en gran medida de la capacidad de las instituciones para articular alianzas intersectoriales y adoptar estándares abiertos. La soberanía pedagógica exige construir repositorios comunes de recursos didácticos de libre acceso que permitan a los planteles compartir costos de desarrollo y enriquecer mutuamente sus ofertas formativas, consolidando una auténtica red regional de aprendizaje colaborativo que empodere a las futuras generaciones ante los dilemas del porvenir.",
            "El gerente educativo del porvenir es un custodio del pacto social: aquel líder que usa la telemática para acercar oportunidades y humanizar la sociedad del conocimiento."
        ],
        "multimedia_type": "radar_future",
        "discussion_question": "Mirando hacia el año 2030, ¿cuál será la competencia gerencial y humana más decisiva que deberá cultivar un directivo para mantener viva la pertinencia de su centro escolar?",
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
<div style="background: #f8fafc; border: 2px solid #2563eb; border-radius: 12px; padding: 20px; margin: 25px 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.08);">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
    <span style="font-size: 1.6rem;">🎙️</span>
    <div>
      <strong style="font-size: 1.05rem; color: #1e293b; display: block; font-family: sans-serif;">Podcast Educativo Oficial: Fundamentos y Modelos de la Gerencia Educativa</strong>
      <span style="font-size: 0.85rem; color: #475569; font-family: sans-serif;">Ponente: Lic. Emily Leidy Chacón de Romero | Centro Local Anzoátegui — UNA (Duración: 5m 33s)</span>
    </div>
  </div>
  
  <!-- Reproductor Oficial Vocaroo -->
  <div style="margin: 15px 0;">
    <label style="font-size: 0.825rem; font-weight: bold; color: #2563eb; display: block; margin-bottom: 6px; font-family: sans-serif;">
      ▶️ Reproductor Integrado (Escucha Inmediata):
    </label>
    <iframe src="https://vocaroo.com/embed/1i8rKfimqgjM?autoplay=0" style="width: 100%; max-width: 500px; height: 60px; border: 0; border-radius: 8px;" allow="autoplay"></iframe>
  </div>
  
  <!-- Enlace oficial directo Vocaroo -->
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; padding-top: 10px; border-top: 1px dashed #cbd5e1;">
    <a href="https://voca.ro/1i8rKfimqgjM" target="_blank" rel="noopener" style="background: #2563eb; color: #ffffff; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85rem; font-family: sans-serif; display: inline-flex; align-items: center; gap: 6px;">
      🔗 Escuchar en enlace oficial de Vocaroo (https://voca.ro/1i8rKfimqgjM) ↗
    </a>
    <span style="font-size: 0.78rem; color: #64748b; font-family: sans-serif;">Audio digital MP3 | 48 kHz Mono | 333 segundos</span>
  </div>
</div>
'''
    elif m_type == "video":
        return '''
<div style="background: #0f172a; border-radius: 12px; overflow: hidden; margin: 25px 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.15);">
  <div style="background: #1e293b; color: #f8fafc; padding: 12px 18px; font-weight: bold; font-size: 0.95rem; font-family: sans-serif; display: flex; align-items: center; gap: 8px;">
    <span>🎥</span> Video-Exposición Oficial: Habilidades Gerenciales y Liderazgo en Entornos Educativos Basados en Tecnología
  </div>
  <video controls playsinline preload="metadata" style="width: 100%; max-height: 480px; display: block; background: #000;">
    <source src="https://anthony-huice.github.io/blog-gerencia-educativa/assets/video-ponencia-unidad2.mp4" type="video/mp4">
    Su navegador no soporta la reproducción de video HTML5.
  </video>
  <div style="padding: 12px 18px; background: #1e293b; color: #94a3b8; font-size: 0.8rem; font-family: sans-serif;">
    <em>Duración: 5m 33s | Ponente: Ing. Emileidy Chacón | Centro Local Anzoátegui — UNA.</em>
  </div>
</div>
'''
    elif m_type == "table_leadership":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin: 22px 0;">
  <strong style="color: #1e293b; font-size: 0.95rem; display: block; margin-bottom: 10px; font-family: sans-serif;">📊 Matriz Comparativa: Modelos de Gestión Escolar</strong>
  <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; font-family: sans-serif; color: #334155;">
    <thead>
      <tr style="background: #e2e8f0; text-align: left;">
        <th style="padding: 8px 12px; border: 1px solid #cbd5e1;">Dimensión</th>
        <th style="padding: 8px 12px; border: 1px solid #cbd5e1;">Modelo Burocrático Normativo</th>
        <th style="padding: 8px 12px; border: 1px solid #cbd5e1;">Modelo Transformacional Digital</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1; font-weight: bold;">Enfoque Directivo</td>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1;">Fiscalización y cumplimiento estricto.</td>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1;">Facilitación, visión compartida y empatía.</td>
      </tr>
      <tr style="background: #f1f5f9;">
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1; font-weight: bold;">Rol del Campus LMS</td>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1;">Repositorio pasivo de archivos PDF.</td>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1;">Ecosistema colaborativo y dialógico.</td>
      </tr>
      <tr>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1; font-weight: bold;">Cultura del Cambio</td>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1;">Resistencia y aversión al error.</td>
        <td style="padding: 8px 12px; border: 1px solid #cbd5e1;">Innovación situada y aprendizaje continuo.</td>
      </tr>
    </tbody>
  </table>
</div>
'''
    elif m_type == "diagram_arch":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin: 22px 0;">
  <strong style="color: #1e293b; font-size: 0.95rem; display: block; margin-bottom: 10px; font-family: sans-serif;">🏗️ Pila de Infraestructura Telemática del Campus Virtual</strong>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-family: sans-serif; font-size: 0.825rem;">
    <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px;">
      <strong style="color: #1d4ed8; display: block;">1. Red y Enlaces (WAN/ISP)</strong>
      Conectividad redundante, ancho de banda simétrico y baja latencia.
    </div>
    <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 10px; border-radius: 4px;">
      <strong style="color: #047857; display: block;">2. Servidores Cloud</strong>
      Balanceadores de carga, clúster de base de datos y elasticidad.
    </div>
    <div style="background: #fefce8; border-left: 4px solid #eab308; padding: 10px; border-radius: 4px;">
      <strong style="color: #a16207; display: block;">3. Plataforma LMS & LTI</strong>
      Interoperabilidad estándar 1EdTech, SCORM y autenticación segura.
    </div>
  </div>
</div>
'''
    elif m_type == "dashboard_analytics":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin: 22px 0;">
  <strong style="color: #1e293b; font-size: 0.95rem; display: block; margin-bottom: 10px; font-family: sans-serif;">📈 Indicadores Clave del Tablero Analítico (Early Warning)</strong>
  <div style="display: flex; gap: 15px; flex-wrap: wrap; font-family: sans-serif; text-align: center;">
    <div style="flex: 1; min-width: 140px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px;">
      <span style="font-size: 0.75rem; color: #64748b; text-transform: uppercase;">Retención Estimada</span>
      <div style="font-size: 1.6rem; font-weight: bold; color: #10b981;">88.2%</div>
      <span style="font-size: 0.72rem; color: #10b981;">+3.8% con tutoría temprana</span>
    </div>
    <div style="flex: 1; min-width: 140px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px;">
      <span style="font-size: 0.75rem; color: #64748b; text-transform: uppercase;">En Umbral de Riesgo</span>
      <div style="font-size: 1.6rem; font-weight: bold; color: #f59e0b;">24 alumnos</div>
      <span style="font-size: 0.72rem; color: #64748b;">Inactividad > 6 días</span>
    </div>
    <div style="flex: 1; min-width: 140px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px;">
      <span style="font-size: 0.75rem; color: #64748b; text-transform: uppercase;">Tiempo de Feedback</span>
      <div style="font-size: 1.6rem; font-weight: bold; color: #3b82f6;">22 horas</div>
      <span style="font-size: 0.72rem; color: #3b82f6;">Promedio de respuesta</span>
    </div>
  </div>
</div>
'''
    elif m_type == "matrix_ai":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin: 22px 0;">
  <strong style="color: #1e293b; font-size: 0.95rem; display: block; margin-bottom: 10px; font-family: sans-serif;">🧭 Dimensiones de la Gobernanza de IA en la Escuela (UNESCO)</strong>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-family: sans-serif; font-size: 0.825rem;">
    <div style="background: #fdf2f8; border-left: 4px solid #ec4899; padding: 10px; border-radius: 4px;">
      <strong style="color: #be185d; display: block;">1. Evaluación Auténtica</strong>
      Priorizar el razonamiento oral, estudios de caso y defensas dialécticas.
    </div>
    <div style="background: #f5f3ff; border-left: 4px solid #8b5cf6; padding: 10px; border-radius: 4px;">
      <strong style="color: #6d28d9; display: block;">2. Transparencia Ética</strong>
      Declaración explícita del uso de copilotos de IA y citación de prompts.
    </div>
    <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 10px; border-radius: 4px;">
      <strong style="color: #047857; display: block;">3. Equidad de Acceso</strong>
      Garantizar herramientas libres para no segregar por poder adquisitivo.
    </div>
  </div>
</div>
'''
    elif m_type == "radar_future":
        return '''
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin: 22px 0;">
  <strong style="color: #1e293b; font-size: 0.95rem; display: block; margin-bottom: 10px; font-family: sans-serif;">📡 Radar de Tendencias Educativas al Horizonte 2030</strong>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-family: sans-serif; font-size: 0.825rem;">
    <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px;">
      <strong style="color: #1d4ed8; display: block;">Aulas Híbridas Ubicuas</strong>
      Coexistencia fluida entre presencialidad física y participación remota.
    </div>
    <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 10px; border-radius: 4px;">
      <strong style="color: #047857; display: block;">Recursos Educativos Abiertos</strong>
      Currículos sustentados en licencias abiertas Creative Commons (CC).
    </div>
    <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 10px; border-radius: 4px;">
      <strong style="color: #b45309; display: block;">Sostenibilidad Digital</strong>
      Servidores de baja huella de carbono y optimización del gasto energético.
    </div>
  </div>
</div>
'''
    return ""

def generate_entry_body(post):
    multimedia_html = render_multimedia(post)
    ref_items = "".join([f"<li style='margin-bottom: 6px; padding-left: 1.5rem; text-indent: -1.5rem;'>{r}</li>" for r in post["references"]])
    
    paragraphs_html = ""
    # Inject multimedia in the middle of analysis paragraphs
    mid = len(post["analysis_paragraphs"]) // 2
    for idx, p in enumerate(post["analysis_paragraphs"]):
        paragraphs_html += f'<p style="margin-bottom: 16px;">{p}</p>\n'
        if idx == mid - 1:
            paragraphs_html += multimedia_html + "\n"
            
    html = f'''
<!-- Imagen Referencial de Alta Definición -->
<div style="margin-bottom: 25px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
  <img src="{post['image_url']}" alt="{post['image_alt']}" style="width: 100%; height: auto; max-height: 440px; object-fit: cover; display: block;">
  <div style="background: #f1f5f9; padding: 8px 14px; font-size: 0.8rem; color: #64748b; font-style: italic; border-top: 1px solid #e2e8f0;">
    {post['image_caption']}
  </div>
</div>

<!-- Cabecera Metafórica Conceptual -->
<div style="background: linear-gradient(135deg, #1e293b, #0f172a); color: #ffffff; padding: 20px 22px; border-radius: 10px; border-left: 5px solid #2563eb; margin-bottom: 22px;">
  <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #93c5fd; font-weight: bold; margin-bottom: 6px;">
    Metáfora Visual: {post['metaphor_title']}
  </div>
  <p style="font-style: italic; font-size: 0.925rem; line-height: 1.55; margin: 0; color: #f8fafc;">
    «{post['metaphor_caption']}»
  </p>
</div>

<!-- Bloque 1: Contexto y Disparador -->
<div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 16px 20px; border-radius: 0 8px 8px 0; margin-bottom: 22px;">
  <div style="font-size: 0.8rem; font-weight: bold; text-transform: uppercase; color: #1e40af; margin-bottom: 6px; letter-spacing: 0.04em;">
    ⚡ Hecho Noticioso & Disparador Contextual
  </div>
  <p style="margin: 0; font-size: 0.95rem; color: #1e293b; line-height: 1.6; font-style: italic;">
    {post['context_trigger']}
  </p>
</div>

<!-- Bloque 2: Análisis Crítico Fundamentado -->
<div style="font-size: 1.025rem; line-height: 1.75; color: #1e293b; text-align: justify;">
  {paragraphs_html}
</div>

<!-- Bloque 3: Pregunta de Discusión y Debate -->
<div style="background: #ecfdf5; border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 10px; padding: 18px 22px; margin: 25px 0 18px;">
  <div style="font-size: 0.8rem; font-weight: bold; color: #047857; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">
    💬 Espacio de Interacción & Debate en Comentarios
  </div>
  <p style="font-size: 1.05rem; font-weight: bold; line-height: 1.45; color: #064e3b; margin: 0 0 10px 0;">
    {post['discussion_question']}
  </p>
  <p style="font-size: 0.825rem; color: #047857; margin: 0; font-style: italic;">
    ✍️ Comparte tu respuesta, reflexión crítica o experiencia formativa en la caja de comentarios al pie de esta publicación.
  </p>
</div>

<!-- Referencias Normadas APA 7.ª Edición -->
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
    
    print("Validando y generando entradas optimizadas...")
    for post in POSTS:
        i = post["id"]
        title = post["title"]
        tags_str = ", ".join(post["tags"])
        body = generate_entry_body(post)
        
        clean_text = re.sub(r'<[^>]+>', ' ', body)
        words = re.findall(r'\b\w+\b', clean_text)
        print(f"Post {i} [{post['date'][:10]}]: {len(words)} palabras | Tags: {tags_str}")
        
        filename = f"Entrada_{i}_{post['tags'][0]}.html"
        filepath = os.path.join(out_dir, filename)
        
        content = f'''<!-- 
================================================================================
ENTRADA #{i} PARA BLOGGER (BLOGSPOT)
FECHA: {post['date']}
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

    # Master XML import
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
    print(f"\n¡Éxito! Archivo maestro exportado en: {xml_path}")

if __name__ == "__main__":
    main()
