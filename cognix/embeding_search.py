def search_database(query):
    data_base = {
    "/Users/laksh4mac/Downloads/lakshpython/rag/atom.txt": """
Topic: atoms and classification of elemental molecules by atomicity.
It is the smallest particle of an element that takes part in a chemical reaction?
This file defines an atom as the smallest particle of an element that takes part in a chemical reaction. It also states that every element is made of the same kind of atoms. The main focus is classification of elements according to the number of atoms present in their elemental molecules: monoatomic, diatomic, tetra-atomic, and octa-atomic.

It identifies monoatomic elements as helium, neon, argon, krypton, xenon, radon, and metals. It identifies diatomic elements as hydrogen, oxygen, nitrogen, fluorine, chlorine, bromine, and iodine. It gives phosphorus, arsenic, and antimony as tetra-atomic elements, written as P4, As4, and Sb4. It gives sulphur as an octa-atomic element, written as S8.

Useful student questions: What is an atom? What is the smallest particle of an element that participates in a chemical reaction? What are monoatomic elements? Which elements exist as diatomic molecules? Why are hydrogen and oxygen written as H2 and O2? What are tetra-atomic elements? Why is sulphur written as S8? Which elements have atomicity 1, 2, 4, or 8?

Related terms: atom, elemental molecule, atomicity, monoatomic, diatomic, tetra-atomic, octa-atomic, H2, O2, N2, F2, Cl2, Br2, I2, P4, As4, Sb4, S8.

This file focuses on atom definition and categories of elemental molecules according to atomicity. It differs from atomicity.txt, which gives the direct definition of atomicity as the number of atoms in one molecule of an element.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/atomicity.txt": """
Topic: atomicity of elements.

This file defines atomicity as the number of atoms present in one molecule of an element. It provides direct examples of atomicity values: helium has atomicity 1, hydrogen has atomicity 2, ozone has atomicity 3, phosphorus has atomicity 4, and sulphur has atomicity 8.

Useful student questions: What is atomicity? How many atoms are present in one molecule of an element? What is the atomicity of helium? What is the atomicity of hydrogen? What is the atomicity of ozone? What is the atomicity of phosphorus? What is the atomicity of sulphur? Which element has atomicity 1, 2, 3, 4, or 8?

Related terms: atomicity, number of atoms in a molecule, elemental molecule, helium, hydrogen, ozone, phosphorus, sulphur, monoatomic, diatomic, triatomic, tetra-atomic, octa-atomic.

This file is specifically about the numerical atom count in a molecule of an element. It differs from atom.txt, which defines atoms and classifies examples as monoatomic, diatomic, tetra-atomic, and octa-atomic.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/compound.txt": """
Topic: chemical compounds, fixed composition, and chemical separation.

This file defines a compound as a substance made from two or more different elements chemically combined with one another in a fixed proportion by weight. It explains that water contains hydrogen and oxygen in a fixed ratio of 1:8 by weight, or oxygen and hydrogen in the ratio 8:1 by weight. It also explains that carbon dioxide contains carbon and oxygen in the ratio 3:8 by weight.

The file states that the constituents of a compound can be separated only through chemical reactions. Its central concepts are chemical combination, different elements, fixed mass ratio, composition by weight, water, carbon dioxide, and chemical separation.

Useful student questions: What is a compound? How is a compound formed? Are elements in a compound chemically combined? What is meant by fixed proportion by weight? What is the ratio of hydrogen to oxygen in water by weight? What is the carbon-to-oxygen ratio in carbon dioxide? Can the constituents of a compound be separated physically? How are elements separated from a compound?

Related terms: compound, chemical combination, chemically combined, fixed composition, fixed proportion, definite proportion, mass ratio, water, hydrogen, oxygen, carbon dioxide, carbon, chemical reaction.

This file differs from mixture.txt. A compound contains elements chemically combined in fixed proportions, while a mixture contains substances that are not chemically combined.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/electropositive_element.txt": """
Topic: electropositive elements and electron loss.

This file defines electropositive elements as elements that tend to lose electrons. It also states that all highly electropositive elements are metals.

Useful student questions: What is an electropositive element? Which elements tend to lose electrons? What does electropositive mean in chemistry? Are highly electropositive elements metals? What is the relationship between metals and electron loss?

Related terms: electropositive element, electropositivity, tendency to lose electrons, electron loss, metals, highly electropositive metals.

This file focuses on the tendency of elements to lose electrons. It differs from metals.txt, which describes physical properties of metals such as lustre, conductivity, malleability, ductility, and sonority.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/element.txt": """
Topic: chemical elements as basic forms of matter.

This file defines an element as a basic form of matter that cannot be broken down into simpler substances by chemical reactions. It gives hydrogen, nitrogen, and oxygen as examples of elements.

Useful student questions: What is an element? What is a chemical element? Can an element be broken down by a chemical reaction? What are examples of elements? Are hydrogen, nitrogen, and oxygen elements? What is the difference between an element and a compound?

Related terms: element, chemical element, basic form of matter, simple substance, chemical reaction, hydrogen, nitrogen, oxygen.

This file gives the basic definition of an element. It differs from compound.txt, where two or more different elements are chemically combined, and from mixture.txt, where elements or compounds are present without chemical combination.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/element_classification.txt": """
Topic: classification of elements into metals, non-metals, metalloids, and radioactive elements.

This file classifies elements according to their properties. It covers metals, non-metals, metalloids, and radioactive elements. It is a comparison-focused reference that includes characteristic properties, exceptions, and examples.

For metals, the file states that metals are generally solid at room temperature. Mercury is an exception because it is liquid at room temperature. Metals have shining surfaces called lustre. They are generally silvery-grey or golden-yellow. Metals are good conductors of heat and electricity, generally hard, ductile, malleable, and sonorous. Ductile means they can be drawn into long wires without breaking or losing their character. Malleable means they can be extended or deformed by hammering or rolling without losing their character. Sonorous means they produce a ringing sound when hit. Metals generally have high melting and boiling points. Sodium and potassium are exceptions because they are soft. Gallium and caesium are exceptions because they have low melting points, approximately 35 degrees Celsius and 28 degrees Celsius. Examples include gold, silver, copper, iron, and sodium.

For non-metals, the file states that they are gases or solids at room temperature. Bromine is an exception because it is liquid at room temperature. Non-metals are usually non-lustrous, but iodine crystals have bright lustre. They are mostly poor conductors of heat and electricity, but graphite conducts electricity. Most non-metals are soft and have lower density than metals, while diamond is extremely hard. Non-metals are non-malleable, non-ductile, and non-sonorous. Their melting and boiling points are generally lower than those of metals, with diamond listed as an exception. Gaseous examples include hydrogen, oxygen, and nitrogen. Solid examples include iodine, carbon in the form of coal or coke, phosphorus, and sulphur.

The file defines metalloids as elements that exhibit properties of both metals and non-metals. It lists germanium, arsenic, antimony, tellurium, and selenium as examples. It defines radioactive elements as elements that emit radiation and lists uranium, polonium, radium, and radon.

Useful student questions: How are elements classified? What are the properties of metals? What are the properties of non-metals? Which metal is liquid at room temperature? Which non-metal is liquid at room temperature? Which non-metal conducts electricity? Why is graphite an exception among non-metals? Which non-metal is very hard? What are ductility, malleability, lustre, and sonority? What are metalloids? Which elements have both metallic and non-metallic properties? What are radioactive elements? Which elements emit radiation? What are the exceptions to the general properties of metals and non-metals?

Related terms: metal, non-metal, metalloid, radioactive element, lustre, conductivity, ductility, malleability, sonority, melting point, boiling point, mercury, sodium, potassium, gallium, caesium, bromine, iodine, graphite, diamond, germanium, arsenic, antimony, tellurium, selenium, uranium, polonium, radium, radon.

This file is broader than metals.txt, non_metals.txt, metalloids.txt, and radioactive_element.txt. Those files focus on one category, while this file compares all four classifications and includes major exceptions.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/element_symbol.txt": """
Topic: chemical symbols, symbol-writing rules, and origins of symbols.

This file explains that elements are represented by symbols, just as common abbreviations such as RBI and ATM represent longer names. It defines a chemical symbol as the shorthand notation of an element. Oxygen is given as an example, represented by O.

The file explains that some elements use the first letter of their English names as a symbol, including hydrogen H, oxygen O, nitrogen N, carbon C, fluorine F, boron B, sulphur S, phosphorus P, iodine I, and uranium U.

It explains the two-letter symbol rule: the first letter is always capitalized and the second letter is lowercase. Cobalt is written as Co, not CO. The file distinguishes Co, the symbol for cobalt, from CO, the formula for carbon monoxide. It includes two-letter symbol examples such as aluminium Al, lithium Li, argon Ar, magnesium Mg, arsenic As, manganese Mn, astatine At, molybdenum Mo, barium Ba, neon Ne, beryllium Be, nickel Ni, bismuth Bi, palladium Pd, and bromine Br.

The file lists symbols derived from Latin or other historical names: antimony Sb from Stibium, copper Cu from Cuprum, gold Au from Aurum, iron Fe from Ferrum, lead Pb from Plumbum, mercury Hg from Hydrargyrum, potassium K from Kalium, silver Ag from Argentum, sodium Na from Natrium, tin Sn from Stannum, and tungsten W from Wolfram.

It also lists elements named after scientists: curium Cm after Madame Curie, einsteinium Es after Albert Einstein, fermium Fm after Enrico Fermi, nobelium No after Alfred Nobel, mendelevium Md after Mendeleev, bohrium Bh after Niels Bohr, and rutherfordium Rf after Rutherford.

It includes elements named after places, countries, or institutions: californium Cf after the University of California, americium Am after America, polonium Po after Poland, francium Fr after France, ruthenium Ru after Russia, and germanium Ge after Germany.

Useful student questions: What is a chemical symbol? What is the symbol of oxygen? What are the rules for writing element symbols? Why is cobalt written as Co and not CO? What does CO represent? Why is sodium written as Na? Why is potassium written as K? What element has the symbol Fe, Au, Ag, Pb, Sn, Sb, Hg, or W? Which element symbols come from Latin names? Which elements are named after scientists? Which elements are named after countries or places?

Related terms: chemical symbol, shorthand notation, capitalization, uppercase letter, lowercase letter, single-letter symbol, two-letter symbol, Latin name, historical name, scientist name, country name, Co, CO, Na, K, Fe, Au, Ag, Pb, Sn, Sb, Hg, W.

This file focuses on how symbols are written and where they come from. It differs from periodic_table.txt, which uses symbols in periodic-table group, block, series, atomic-number, and mnemonic contexts.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/fundamental_particle.txt": """
Topic: fundamental particles of atoms, atomic number, mass number, nucleons, and nuclide notation.

This file identifies electron, proton, and neutron as the three fundamental particles present in an atom. It compares their charge, notation, mass, charge magnitude, and relative charge.

Electron: negative charge, notation e minus, mass 9.11 × 10^-28 grams or 0.000548 amu, charge magnitude negative 1.602 × 10^-19 coulombs or negative 4.8 × 10^-10 esu, and relative charge negative 1.

Proton: positive charge, notation p plus, mass 1.672 × 10^-24 grams or 1.007277 amu, charge magnitude positive 1.602 × 10^-19 coulombs or positive 4.8 × 10^-10 esu, and relative charge positive 1.

Neutron: no charge, notation n zero, mass 1.675 × 10^-24 grams or 1.008665 amu, and no listed charge magnitude or relative charge.

The file gives the neutral atom rule: in a neutral atom, the number of positive charges equals the number of negative charges. Therefore, the number of protons equals the number of electrons in a neutral atom.

It defines atomic number as the number of protons inside the nucleus, or the number of electrons outside the nucleus in a neutral atom. Atomic number is represented by Z.

It defines mass number as the sum of protons and neutrons in the nucleus. Mass number is represented by A. It states that protons and neutrons together are called nucleons. It gives the equations A = number of protons + number of neutrons, A = Z + n, and n = A - Z.

The file also gives nuclide notation in the form ZXA, where X represents the element, A represents the mass number, and Z represents the atomic number.

Useful student questions: What are the three fundamental particles? What charge does an electron, proton, or neutron have? What is the mass of an electron? Which particle has no charge? What is a neutral atom? Why are proton and electron numbers equal in a neutral atom? What is atomic number? What does Z represent? What is mass number? What does A represent? What are nucleons? How do I calculate the number of neutrons? What is the formula n = A - Z? How is an element written using atomic number and mass number?

Related terms: electron, proton, neutron, subatomic particle, fundamental particle, nucleus, charge, relative charge, atomic mass unit, amu, atomic number, mass number, nucleon, neutral atom, nuclide notation, Z, A, n.

This file is the detailed atomic-structure reference. It differs from atom.txt, which defines an atom and classifies elements by atomicity, and from atomicity.txt, which counts atoms in elemental molecules.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/matter.txt": """
Topic: matter, mass, volume, particles, and radiation.

This file introduces the universe as consisting of matter and radiation. It gives sunlight and starlight as examples of radiation. It identifies air, food, stones, clouds, stars, plants, animals, water, and sand as matter.

The file defines matter as anything that has mass and occupies space. It states that matter has both mass and volume. It also states that matter is made of particles and that particles of matter are extremely small. It gives the example that more than 10^20 particles are present in the full stop of a sentence.

Useful student questions: What is matter? What are the characteristics of matter? Does matter have mass? Does matter occupy space? What is volume? What is matter made of? Are air, water, plants, animals, sand, and stones matter? Is sunlight matter or radiation? Are stars matter? How small are particles of matter?

Related terms: matter, radiation, mass, volume, occupies space, particles of matter, sunlight, starlight, air, water, food, stones, clouds, plants, animals, sand.

This file is a general introduction to matter. It differs from element.txt, compound.txt, and mixture.txt, which classify specific kinds of matter.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/metalloids.txt": """
Topic: metalloids, also called semimetals.

This file defines metalloids as elements that exhibit properties of both metals and non-metals. It lists germanium, arsenic, antimony, tellurium, and selenium as examples.

Useful student questions: What are metalloids? What are semimetals? Which elements show properties of both metals and non-metals? Is germanium a metalloid? Is arsenic a metalloid? Is antimony a metalloid? Is tellurium a metalloid? Is selenium a metalloid?

Related terms: metalloid, semimetal, properties of metals, properties of non-metals, germanium, arsenic, antimony, tellurium, selenium.

This is a concise metalloid definition-and-examples file. It differs from element_classification.txt, which compares metals, non-metals, metalloids, and radioactive elements with their properties and exceptions.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/metals.txt": """
Topic: characteristic physical properties and examples of metals.

This file explains that metals are generally solids at room temperature. Mercury is listed as an exception because it is a metal that is liquid at room temperature. Metals have a shining surface, known as lustre. They are generally silvery-grey or golden-yellow in colour.

The file states that metals are good conductors of heat and electricity. They are generally hard, although sodium and potassium are exceptions because they are soft. Metals are ductile, meaning they can be drawn into long wires without breaking and without losing their character. Metals are malleable, meaning they can be extended or deformed by hammering or rolling without losing their character. Metals are sonorous, meaning they make a ringing sound when hit.

The file states that metals usually have high melting and boiling points. Gallium and caesium are exceptions, with melting points listed as 35 degrees Celsius and 28 degrees Celsius. Examples given are gold, silver, copper, iron, and sodium.

Useful student questions: What are the properties of metals? What is lustre? Which metal is liquid at room temperature? Which metals are soft? What does ductile mean? What does malleable mean? What does sonorous mean? Are metals good conductors of electricity? Are metals good conductors of heat? Why can metals be made into wires? Why can metals be hammered into sheets? Which metals have low melting points? What are examples of metals?

Related terms: metal, solid, mercury, lustre, shiny surface, conductor, heat conductor, electrical conductor, hardness, sodium, potassium, ductility, ductile, malleability, malleable, sonority, sonorous, melting point, boiling point, gallium, caesium, gold, silver, copper, iron.

This file focuses only on metals. It differs from non_metals.txt, which describes non-metal properties, and element_classification.txt, which compares metals with other element classes.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/mixture.txt": """
Topic: mixtures and substances that are not chemically combined.

This file defines a mixture as a substance consisting of two or more elements or compounds of different types that are not chemically combined together. It gives sodium chloride in water, sand in water, chalk in water, and air as examples.

Useful student questions: What is a mixture? Are substances in a mixture chemically combined? Is salt water a mixture? Is sand in water a mixture? Is chalk in water a mixture? Is air a mixture? Can a mixture contain elements and compounds? What is the difference between a mixture and a compound?

Related terms: mixture, uncombined substances, not chemically combined, sodium chloride in water, salt water, sand in water, chalk in water, air, elements, compounds.

This file differs from compound.txt. In a mixture, substances are not chemically combined; in a compound, different elements are chemically combined in fixed proportions by weight.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/molecule.txt": """
Topic: molecules as independently existing particles of elements or compounds.

This file defines a molecule as the smallest particle of an element or compound that has independent existence and retains all the properties of that element or compound. It gives H2, O2, N2, H2O, and CO2 as examples.

Useful student questions: What is a molecule? What is the smallest independently existing particle of an element? What is the smallest independently existing particle of a compound? Can a molecule retain the properties of a substance? Is H2 a molecule? Is O2 a molecule? Is N2 a molecule? Is water H2O a molecule? Is carbon dioxide CO2 a molecule?

Related terms: molecule, independently existing particle, smallest particle, properties of an element, properties of a compound, H2, O2, N2, H2O, CO2.

This file defines molecules broadly for both elements and compounds. It differs from atomicity.txt, which counts atoms in one molecule of an element, and atom.txt, which defines atoms and groups elemental molecules by atomicity.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/non_metals.txt": """
Topic: characteristic physical properties and examples of non-metals.

This file explains that non-metals are gases or solids at room temperature. Bromine is listed as an exception because it is liquid at room temperature. Non-metals are usually non-lustrous, although iodine crystals have bright lustre.

The file states that non-metals are mostly poor conductors of heat and electricity. Graphite is listed as an exception because it is a good conductor of electricity. Most non-metals are soft and have lower densities than metals. Diamond is an exception because it is very hard and is described as probably the hardest substance.

Non-metals are non-malleable, non-ductile, and non-sonorous. Their melting and boiling points are generally lower than those of metals. Diamond is listed as an exception.

Examples of gaseous non-metals are hydrogen, oxygen, and nitrogen. Examples of solid non-metals are iodine, carbon in the forms of coal and coke, phosphorus, and sulphur.

Useful student questions: What are the properties of non-metals? Are non-metals solids, liquids, or gases? Which non-metal is liquid at room temperature? Which non-metal has lustre? Which non-metal conducts electricity? Why is graphite an exception among non-metals? Which non-metal is extremely hard? Are non-metals malleable? Are non-metals ductile? Are non-metals sonorous? Give examples of gaseous non-metals. Give examples of solid non-metals.

Related terms: non-metal, bromine, iodine, graphite, diamond, conductivity, poor conductor, lustre, density, hardness, brittle, non-malleable, non-ductile, non-sonorous, hydrogen, oxygen, nitrogen, carbon, coal, coke, phosphorus, sulphur.

This file focuses only on non-metals and their exceptions. It differs from metals.txt and from element_classification.txt, which compares non-metals against metals, metalloids, and radioactive elements.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/periodic_table.txt": """
Topic: periodic table, periodic classification, element groups, blocks, families, atomic numbers, and Hindi/Hinglish element mnemonics.

This file is an extensive periodic-table learning guide. It defines the periodic table as an ordered chart of all 118 known chemical elements arranged in increasing atomic number. Its main purpose is to help students identify element categories, learn group and block sequences, remember symbols and atomic numbers, and memorize element orders through Hindi and Hinglish mnemonics.

The file includes a five-step teaching method for explaining periodic-table mnemonics. The method asks the teacher to set a visual scene or story hook, present the Hindi and Hinglish sentence, map Hindi words or syllables to symbols and then element names, highlight Latin-symbol and phonetic traps, and teach the atomic-number gap sequence down groups: +2, +8, +8, +18, +18, +32.

The file classifies post-transition metals as soft or brittle metals with poor mechanical strength. The listed post-transition metals are aluminium Al with atomic number 13, gallium Ga 31, indium In 49, tin Sn 50, thallium Tl 81, lead Pb 82, bismuth Bi 83, nihonium Nh 113, flerovium Fl 114, moscovium Mc 115, and livermorium Lv 116.

The file lists metalloids, also called semimetals, as elements with properties intermediate between metals and non-metals. Its metalloid list contains boron B 5, silicon Si 14, germanium Ge 32, arsenic As 33, antimony Sb 51, tellurium Te 52, and polonium Po 84.

The file lists reactive non-metals that are not halogens or noble gases: hydrogen H 1, carbon C 6, nitrogen N 7, oxygen O 8, phosphorus P 15, sulfur S 16, and selenium Se 34.

Group 1, the alkali metals in the s-block, is described as highly reactive metals. Hydrogen is placed in Group 1 but described as a non-metal because of its 1s1 configuration. The order is hydrogen H 1, lithium Li 3, sodium Na 11, potassium K 19, rubidium Rb 37, caesium Cs 55, and francium Fr 87. The principal mnemonic is Halina ki rab se fariyaad. The guide explains the symbol traps Na from Natrium for sodium, K from Kalium for potassium, and Cs for caesium rather than Se for selenium.

Group 2, alkaline earth metals in the s-block, is described as reactive metals that are less reactive than alkali metals. The order is beryllium Be 4, magnesium Mg 12, calcium Ca 20, strontium Sr 38, barium Ba 56, and radium Ra 88. The main Hindi mnemonic is Beta maange car scooter baap raazi, with an alternative mnemonic also included. The guide warns students not to confuse Sr for strontium with Sc for scandium.

Group 13, the boron family in the p-block, includes boron B, aluminium Al, gallium Ga, indium In, thallium Tl, and notes nihonium Nh as element 113. The main mnemonic is Baingan aloo gajar in thaila. It highlights that boron is a metalloid and warns students not to confuse Tl for thallium with Th for thorium.

Group 14, the carbon family in the p-block, includes carbon C, silicon Si, germanium Ge, tin Sn, lead Pb, and notes flerovium Fl as element 114. The main mnemonic is Kahe Sita ji suno prabhu. It highlights that Sn comes from Stannum and represents tin, while Pb comes from Plumbum and represents lead.

Group 15, the nitrogen family or pnictogens in the p-block, includes nitrogen N, phosphorus P, arsenic As, antimony Sb, bismuth Bi, and notes moscovium Mc as element 115. The main mnemonic is Nana Patekar Asrani sab bimaar. The guide identifies arsenic as a metalloid, bismuth as a metal, and explains that Sb is derived from Stibium and represents antimony.

Group 16, the oxygen family or chalcogens in the p-block, includes oxygen O, sulfur S, selenium Se, tellurium Te, polonium Po, and notes livermorium Lv as element 116. The main mnemonic is Old style se tee po. The guide identifies tellurium as a metalloid and polonium as radioactive.

Group 17, the halogens in the p-block, are described as highly reactive non-metals. The order is fluorine F 9, chlorine Cl 17, bromine Br 35, iodine I 53, astatine At 85, with tennessine Ts noted as element 117. The mnemonic is Fir kal bahar aayi aunty. The guide notes that fluorine is the most electronegative element, bromine is the only liquid non-metal at room temperature, iodine is a lustrous solid non-metal, and astatine is a radioactive halogen.

Group 18, noble gases in the p-block, are described as inert and extremely stable gases. The order is helium He 2, neon Ne 10, argon Ar 18, krypton Kr 36, xenon Xe 54, radon Rn 86, with oganesson Og noted as element 118. The mnemonic is Heena Neena aur Kareena ki X-ray rangeen. The guide identifies radon as radioactive.

The file describes d-block transition metals, Groups 3 to 12, as hard and dense metals with high melting and boiling points. It explains that transition-metal series are memorized horizontally across a period rather than vertically down a group.

The 3d transition series, Period 4 and atomic numbers 21 to 30, contains scandium Sc 21, titanium Ti 22, vanadium V 23, chromium Cr 24, manganese Mn 25, iron Fe 26, cobalt Co 27, nickel Ni 28, copper Cu 29, and zinc Zn 30. It provides a Hindi mnemonic and an alternative popular mnemonic. It warns students not to confuse Mn for manganese with Mg for magnesium. It also explains that the mnemonic word Feko represents both Fe for iron and Co for cobalt.

The 4d transition series, Period 5 and atomic numbers 39 to 48, contains yttrium Y 39, zirconium Zr 40, niobium Nb 41, molybdenum Mo 42, technetium Tc 43, ruthenium Ru 44, rhodium Rh 45, palladium Pd 46, silver Ag 47, and cadmium Cd 48. The mnemonic is Yaari zara nibha maut tak rukawat raah mein pade to aag mein kood ja. It identifies technetium as the first synthetic element and explains Ag as the Latin-derived symbol for silver from Argentum.

The 5d transition series, Period 6, includes lanthanum La 57, then the lanthanide sequence 58 to 71, followed by hafnium Hf 72, tantalum Ta 73, tungsten W 74, rhenium Re 75, osmium Os 76, iridium Ir 77, platinum Pt 78, gold Au 79, and mercury Hg 80. Its mnemonic is La hafta warna re us iron rod se pitega aur hospital jayega. The guide states that tungsten uses W from Wolfram, gold uses Au from Aurum, and it warns that Ir in the mnemonic refers to iridium rather than Fe for iron. It identifies osmium as the densest natural element.

The 6d transition series, Period 7 and atomic numbers 104 to 112, includes rutherfordium Rf 104, dubnium Db 105, seaborgium Sg 106, bohrium Bh 107, hassium Hs 108, meitnerium Mt 109, darmstadtium Ds 110, roentgenium Rg 111, and copernicium Cn 112.

The file identifies f-block elements as inner transition metals. The lanthanide series, also called the 4f series with atomic numbers 57 to 71, is described as rare earth elements. It lists lanthanum La, cerium Ce, praseodymium Pr, neodymium Nd, promethium Pm, samarium Sm, europium Eu, gadolinium Gd, terbium Tb, dysprosium Dy, holmium Ho, erbium Er, thulium Tm, ytterbium Yb, and lutetium Lu. It includes a Hindi mnemonic and maps each mnemonic syllable to its element symbol and element name.

The actinide series, also called the 5f series with atomic numbers 89 to 103, is described as radioactive elements. It lists actinium Ac, thorium Th, protactinium Pa, uranium U, neptunium Np, plutonium Pu, americium Am, curium Cm, berkelium Bk, californium Cf, einsteinium Es, fermium Fm, mendelevium Md, nobelium No, and lawrencium Lr. It includes a Hindi mnemonic and maps each syllable to its corresponding symbol and element.

Useful student questions: What is the periodic table? How are elements arranged in the periodic table? What are s-block, p-block, d-block, and f-block elements? What are alkali metals? What are alkaline earth metals? What are the boron, carbon, nitrogen, oxygen, halogen, and noble-gas families? What are pnictogens? What are chalcogens? How can I memorize Group 1? How can I memorize Group 2? What is the Hindi mnemonic for the carbon family? What are the 3d transition elements in order? What are the 4d and 5d transition series? What are the lanthanides? What are the actinides? What are the atomic-number gaps down a group? Why is potassium represented by K? Why is tin represented by Sn? Why is lead represented by Pb? Why is tungsten represented by W? Why is gold represented by Au? Which elements are metalloids? Which elements are radioactive?

Related terms: periodic table, atomic number, element symbol, groups, periods, blocks, s-block, p-block, d-block, f-block, alkali metals, alkaline earth metals, boron family, carbon family, nitrogen family, pnictogens, oxygen family, chalcogens, halogens, noble gases, transition metals, post-transition metals, lanthanides, actinides, rare earth elements, radioactive elements, Hindi mnemonic, Hinglish mnemonic, symbol trap, Latin symbol, atomic-number gap.

This file is the comprehensive periodic-table and mnemonic study guide. It differs from element_symbol.txt, which focuses on symbol rules and symbol origins, and from the separate metals, non-metals, metalloids, and radioactive-elements files, which provide shorter category-specific descriptions.
""",

    "/Users/laksh4mac/Downloads/lakshpython/rag/radioactive_element.txt": """
Topic: radioactive elements and emission of radiation.

This file defines radioactive elements as elements that emit radiation. It lists uranium, polonium, radium, and radon as examples.

Useful student questions: What is a radioactive element? Which elements emit radiation? What is radioactivity? Give examples of radioactive elements. Are uranium, polonium, radium, and radon radioactive?

Related terms: radioactive element, radioactivity, radiation, uranium, polonium, radium, radon.

This is a concise radioactive-elements definition file. It differs from element_classification.txt, which includes radioactive elements as one category among metals, non-metals, and metalloids, and from periodic_table.txt, which places radioactive elements within periodic-table groups and series.
"""
}
    from pathlib import Path
    from sentence_transformers import SentenceTransformer
    import numpy as np

    model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5")

    paths = list(data_base)
    descriptions = list(data_base.values())

    description_vectors = model.encode(
    [
        f"Topic: {Path(path).stem.replace('_', ' ')}. {description}"
        for path, description in data_base.items()
    ],
    normalize_embeddings=True
)
    query_vector = model.encode(
        query,
        normalize_embeddings=True
    )

    scores = description_vectors @ query_vector
    best_matches = int(np.argmax(scores))

    return paths[best_matches]