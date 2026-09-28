#!/usr/bin/env python3
"""Write the per-subject briefs for the cybernetic_elite set into briefs/. Each brief is the
subject-specific half of the prompt; the shared half is PROMPT_TEMPLATE_CYBERNETIC_ELITE.md.
Roster: every person, institution, program and text named in "The Unabomber & the Net:
Kaczynski, Epstein and the Cybernetic Elite" (Hidden AmuraKa, 2026, https://youtu.be/WEnSnCYoeqk)
that did not already have a dossier anywhere in symbols/ or the atlas on 2026-09-28.
Already held elsewhere and therefore NOT here: Jeffrey Epstein, Ghislaine Maxwell, Peter Thiel,
Reid Hoffman, Marc Andreessen, Alex Karp, Nick Land, Bill Gates, Norbert Wiener, Claude Shannon,
John von Neumann, John Cage, Richard Dawkins."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "briefs"); os.makedirs(OUT, exist_ok=True)

# slug: (name, class, role in the video's network, threads to pull)
SIGNS = {
 # --- the bomber, his targets, his family ---
 "theodore_kaczynski": ("Theodore J. Kaczynski", "person (mathematician, domestic terrorist, author)",
  "the film's first pole: the man who attacked the specialists of the emerging technological system",
  "Harvard 1958-62 at sixteen; Henry Murray's 'Multiform Assessments of Personality Development Among Gifted College Men' (code name 'Lawful', Kaczynski's subject code), consent, funding (verify or refute the CIA/MKUltra claim: Alston Chase, Harvard and the Unabomber, 2003, versus the Murray Research Archive record); Michigan PhD 1967 (boundary functions), Berkeley assistant professorship 1967-69; the Lincoln, Montana cabin 1971; the sixteen bombings 1978-95 with each target and injury; the 1995 letters to the New York Times and Washington Post, the naming of Roberts and Sharp, the publication of 'Industrial Society and Its Future' (Sept 19 1995); David Kaczynski and Linda Patrik's recognition, the FBI UNABOM task force, arrest April 3 1996; the plea 1998, ADX Florence, death June 10 2023 (medical center Butner, ruled suicide); the correspondence archive at Michigan's Labadie Collection; 'Technological Slavery', 'Anti-Tech Revolution'; the online 'Uncle Ted' reception; the cabin's ownership and display at the Newseum"),
 "david_gelernter": ("David Gelernter", "person (computer scientist, Yale)",
  "bombed June 24 1993; the specialist Kaczynski named; later in Brockman's Edge and, per 2026 releases, in Epstein's correspondence 2009-15",
  "Linda coordination language (with Nicholas Carriero), 'Mirror Worlds' (1991) and the phrase and its afterlife in 'digital twin' discourse; the June 24 1993 bomb, injuries, the letter Kaczynski sent him in April 1995; 'Drawing Life' (1997); Lifestreams and Mirror Worlds Technologies, the patent suit against Apple (2010 verdict, later reversed); Scopeware; art and criticism, his 'Americanism' and 'America-Lite' (2012), National Council on the Arts, consideration for Trump science adviser 2017; the 2026 document release: Brockman's introduction (Dec 2009), the 2011 recommendation of a Yale undergraduate to Epstein and his stated defense, Yale's review and his removal from teaching, his message to students; the Edge Foundation ties; his brother Joel; what the released emails actually say and which outlets carried them"),
 "joel_gelernter": ("Joel Gelernter", "person (psychiatric geneticist, Yale / VA Connecticut)",
  "David Gelernter's brother, named in 1993 as receiving an additional threat after the bombing",
  "his career in psychiatric genetics at Yale and the West Haven VA; the 1993 threatening letter and police protection reported in June 1993; whether any later connection to Edge or Epstein exists (verify, do not assume); keep the dossier to what is documented"),
 "charles_epstein_geneticist": ("Charles J. Epstein", "person (medical geneticist, UCSF)",
  "bombed June 22 1993, two days before Gelernter; the geneticist named alongside the computer scientist in Kaczynski's 1995 letters",
  "UCSF Down syndrome and trisomy research, the June 22 1993 bomb at his Tiburon home and injuries, his public statements, editorship of the American Journal of Human Genetics, death 2011; distinguish him carefully and explicitly from Jeffrey Epstein throughout; Kaczynski's 1995 explanation of why geneticists were targets"),
 "james_mcconnell": ("James V. McConnell", "person (psychologist, University of Michigan)",
  "bombed November 15 1985 with his assistant Nicklaus Suino; behavior modification as target",
  "planarian memory-transfer experiments and 'The Worm Runner's Digest', 'Understanding Human Behavior', his advocacy of behavior modification and the 1970 Psychology Today essay Kaczynski is said to have objected to; the 1985 bomb disguised as a manuscript, injuries to McConnell and Suino, his death 1990"),
 "nicklaus_suino": ("Nicklaus Suino", "person (McConnell's research assistant, later martial-arts author)",
  "injured opening the 1985 bomb addressed to McConnell",
  "the November 1985 bombing and his injuries, his later career and his own account of the attack"),
 "hugh_scrutton": ("Hugh Scrutton", "person (Sacramento computer-store owner)",
  "first person killed, December 11 1985",
  "RenTech Computer Rentals, the bomb outside the store, the investigation, his family and their statements at the 1998 sentencing"),
 "thomas_mosser": ("Thomas J. Mosser", "person (Burson-Marsteller / Young & Rubicam executive)",
  "killed December 10 1994; Kaczynski's stated reason concerned Burson-Marsteller and Exxon Valdez publicity",
  "his career at Burson-Marsteller and Young & Rubicam, the North Caldwell bomb, Kaczynski's April 1995 letter explaining the target and its factual error about Exxon, the family's later statements"),
 "gilbert_murray_forester": ("Gilbert Brent Murray", "person (president, California Forestry Association)",
  "killed April 24 1995, the last victim",
  "the California Forestry Association, the package addressed to his predecessor William Dennison, his family's statements and Connie Murray's testimony at sentencing"),
 "richard_j_roberts": ("Richard J. Roberts", "person (molecular biologist, 1993 Nobel laureate)",
  "named with Phillip Sharp in Kaczynski's April 1995 letter to the New York Times as prospective targets",
  "split genes and RNA splicing (Nobel 1993 with Sharp), Cold Spring Harbor, New England Biolabs; the April 1995 Unabomber letter's naming of him, his reaction, security measures; later public positions (GMO letter of Nobel laureates 2016)"),
 "phillip_sharp": ("Phillip A. Sharp", "person (molecular biologist, MIT, 1993 Nobel laureate)",
  "named with Roberts in Kaczynski's 1995 letter",
  "RNA splicing, MIT Center for Cancer Research, co-founder of Biogen (1978) and Alnylam; the 1995 letter naming him and his response; his boards and biotech investments as part of the network of science and capital"),
 "david_kaczynski": ("David Kaczynski", "person (brother of the bomber, social worker, anti-death-penalty advocate)",
  "recognized the manifesto's voice and turned his brother in through attorney Anthony Bisceglie",
  "the family history in Evergreen Park, his own years in the Texas desert, Linda Patrik's suspicion, the linguistic comparison, the FBI approach, the $1 million reward and its donation to victims, 'Every Last Tie' (2016), his work with New Yorkers for Alternatives to the Death Penalty, his statements at Ted's death"),
 "linda_patrik": ("Linda Patrik", "person (philosophy professor, Union College; David Kaczynski's wife)",
  "first suspected the Unabomber was Ted Kaczynski",
  "her account of reading the manifesto, her role in persuading David, her academic work; keep to the documented record"),

 # --- the filmmaker and the map ---
 "lutz_dammbeck": ("Lutz Dammbeck", "person (German filmmaker and artist)",
  "made 'Das Netz' (The Net, 2003), the map of the network the video follows",
  "East German media-art origins, 'Herakles Konzept', Dresden and Hamburg; 'Das Netz: Die Konstruktion des Unabombers' (2003), its interviews (Brand, Gelernter, Brockman, Heinz von Foerster, Rauschenberg, John Markoff, Bill Joy, Robert Taylor), its correspondence with Kaczynski from prison, the book 'Das Netz' (Edition Nautilus 2005), 'Overgames' (2015); the film's thesis on Macy cybernetics, the counterculture and the CIA; critical reception in Germany and the US"),
 "the_net_film_2003": ("The Net (Das Netz), 2003 film", "text/film",
  "the source map: Dammbeck's network diagram of scientists, publishers, technologists",
  "production, structure, every interviewee and their claims on camera, the prison letters, the wall-diagram device, distribution (Other Cinema DVD 2006), reviews, and what the film asserted about the Murray experiment, LSD and the CIA versus what is documented"),

 # --- Harvard and the Murray experiment ---
 "henry_murray": ("Henry A. Murray", "person (psychologist, Harvard; OSS)",
  "ran the Harvard personality experiments in which Kaczynski was a subject 1959-62",
  "Harvard Psychological Clinic, 'Explorations in Personality' (1938), the Thematic Apperception Test with Christiana Morgan, his OSS assessment work 1943-45 and the analysis of Hitler; the 1959-62 'Multiform Assessments' study, the 'dyadic' stress interviews, subject codes, funding sources (verify the claimed federal and Rockefeller/NIMH support and any CIA or MKUltra link, citing Chase 2003, the Murray Research Archive, and refutations); his LSD interest and the Timothy Leary/Harvard Psilocybin context; his papers and the sealed subject data"),
 "murray_harvard_experiment": ("The Murray Harvard Experiments (Multiform Assessments of Personality Development Among Gifted College Men, 1959-62)", "program",
  "the study that enrolled Kaczynski as 'Lawful'",
  "design (the 'dyad' with an aggressive confederate lawyer, filmed sessions, replay of humiliation), the twenty-two subjects, funding, consent forms, the Murray Research Archive holdings and access rules, what Kaczynski himself said of it (and dismissed), Alston Chase's Atlantic essay (June 2000) and book (2003), the responses of Murray's colleagues and of Harvard; the MKUltra claim traced to its sources and weighed"),
 "mkultra": ("MKUltra", "program (CIA behavioral research, 1953-73)",
  "the claim that Murray's study or the Macy cybernetics circle connected to CIA mind-control funding",
  "Sidney Gottlieb, the 1975 Church Committee and Rockefeller Commission, the 1977 Senate hearings after the MKULTRA files surfaced, the funding conduits (Society for the Investigation of Human Ecology, Geschickter Fund, Josiah Macy Jr. Foundation as alleged conduit), universities involved, Harvard's documented and undocumented involvement, Frank Olson; which claims about Murray, Leary or the Macy Foundation are documented and which are inference"),
 "arthur_k_solomon": ("Arthur K. Solomon", "person (biophysicist, Harvard)",
  "the 'A.K. Solomon' whose call Stewart Brand recalls in the film, a Harvard biophysics figure of the Macy period",
  "founder of Harvard's biophysics program, Manhattan Project, his connections to the Macy circle and to Brand (Brand studied biology at Stanford; verify the film's anecdote), Harvard's Committee on Higher Degrees in Biophysics; documentation over anecdote"),

 # --- Macy cybernetics and its circle (Wiener, Shannon, von Neumann held elsewhere) ---
 "macy_conferences": ("The Macy Conferences on Cybernetics (1946-53)", "program/event",
  "the founding circle of cybernetics in the film's genealogy",
  "the Josiah Macy Jr. Foundation and Frank Fremont-Smith, the ten conferences, participants (Wiener, von Neumann, McCulloch, Pitts, Mead, Bateson, von Foerster, Shannon, Rosenblueth, Kubie, Bigelow, Savage, Northrop, Ashby, Lewin), the proceedings edited by von Foerster, Mead and Teuber; Steve Heims's 'The Cybernetics Group' (1991) and Jean-Pierre Dupuy; military funding of participants; the Macy Foundation's LSD conferences (1959) and the CIA-conduit allegation; what the film claims versus what Heims documents"),
 "warren_mcculloch": ("Warren S. McCulloch", "person (neurophysiologist, cybernetician)",
  "chaired the Macy conferences; McCulloch-Pitts neuron",
  "'A Logical Calculus of the Ideas Immanent in Nervous Activity' (1943 with Walter Pitts), Illinois Neuropsychiatric Institute, MIT Research Laboratory of Electronics, funding by ONR and the military, 'Embodiments of Mind' (1965), his Wittgenstein quotation and philosophical style, the break with Wiener (1952), the Chicago Literary Club addresses"),
 "margaret_mead": ("Margaret Mead", "person (anthropologist)",
  "Macy participant; with Bateson carried cybernetics into social science",
  "Samoa and New Guinea fieldwork, the Bateson marriage, the Macy conferences and the coining of 'cybernetics' anecdote, 'Cybernetics of Cybernetics' (1968 ASC address), the American Museum of Natural History, her Cold War government work (RAND, the Committee for National Morale, OSS/OWI-era projects, the CIA-funded Society for the Investigation of Human Ecology grant question), the Freeman controversy; the network ties to Brand, Bateson, Foerster"),
 "gregory_bateson": ("Gregory Bateson", "person (anthropologist, cyberneticist)",
  "Macy participant; the bridge from cybernetics to the counterculture Brand came out of",
  "Naven, Bali with Mead, OSS service in Asia 1943-45 (his own account of disillusion), the Macy conferences, the Palo Alto double-bind schizophrenia project and the Mental Research Institute, the dolphin work with John Lilly, Esalen, 'Steps to an Ecology of Mind' (1972), the CoEvolution Quarterly and Brand friendship, the University of California regents seat under Jerry Brown, Lindisfarne; the documented CIA/LSD adjacency (Lilly, Leary, Ginsberg's claim that Bateson gave him LSD at the Palo Alto VA hospital in 1959) with its sources"),
 "heinz_von_foerster": ("Heinz von Foerster", "person (physicist, cybernetician)",
  "Macy secretary; interviewed in 'The Net' as the last witness",
  "Vienna origins, the Wittgenstein family connection (his mother's circle; verify the claim of kinship), 'Das Gedächtnis' (1948), the Macy conferences as editor, the Biological Computer Laboratory at Illinois (1958-76) and its ONR and Air Force funding, second-order cybernetics, the Whole Earth/CoEvolution connection, the filmed interview with Dammbeck and its content"),
 "marshall_mcluhan": ("Marshall McLuhan", "person (media theorist)",
  "the film's link from cybernetics to media and to Brockman's early career",
  "'The Gutenberg Galaxy' (1962), 'Understanding Media' (1964), the Centre for Culture and Technology, his Catholic conservatism, the IBM and Ford Foundation funding, the 'global village', the relationship with John Brockman and the 1960s expanded-cinema scene (Brockman's 'By the Late John Brockman' 1969), Gerald Feigen and Howard Gossage's promotion; his influence on Brand and Wired"),
 "robert_rauschenberg": ("Robert Rauschenberg", "person (artist)",
  "interviewed in 'The Net'; the art-technology network (E.A.T., Cage, Billy Klüver)",
  "Black Mountain and Cage, Experiments in Art and Technology (1966, with Klüver and Bell Labs), '9 Evenings', the Brockman-organized happenings and 'Expanded Cinema Festival' 1965, what he says on camera in Dammbeck's film; the money: Leo Castelli, the foundation"),

 # --- the counterculture and personal computing ---
 "stewart_brand": ("Stewart Brand", "person (Whole Earth Catalog founder, Long Now)",
  "the film's second pole: from Merry Pranksters to the technological elite; Kaczynski's cabin came from the Catalog's world",
  "Stanford biology, Army, USCO and the Trips Festival (1966), the Merry Pranksters and Ken Kesey, the 'why haven't we seen a photograph of the whole Earth yet' button 1966, the Whole Earth Catalog 1968-72 and its National Book Award, working for Engelbart's 1968 'Mother of All Demos' as camera operator, 'Spacewar' in Rolling Stone (1972), CoEvolution Quarterly, the WELL (1985, with Larry Brilliant), Global Business Network (1987, with Schwartz; the corporate and intelligence clients), the Long Now Foundation (1996, with Hillis), 'How Buildings Learn', 'Whole Earth Discipline' (nuclear, GMO, geoengineering), 'The Media Lab' (1987); Brockman dinners and the 2004 billionaires' dinner with Epstein per Edge's own archive; Fred Turner's 'From Counterculture to Cyberculture' (2006); what he says in 'The Net' about the Catalog, Kaczynski and the A.K. Solomon anecdote; Markoff's biography 'Whole Earth' (2022)"),
 "whole_earth_catalog": ("Whole Earth Catalog (1968-72) and its successors", "text/institution",
  "the tool-book that taught cabin-building and became the counterculture-to-cyberculture conduit",
  "the Portola Institute, Dick Raymond, the editions and their contents (Buckminster Fuller, cybernetics, Wiener, Bateson), the Last Whole Earth Catalog (1971) and its National Book Award, the Demise Party and the $20,000 giveaway, CoEvolution Quarterly, Whole Earth Review, the Point Foundation's money, the Whole Earth Software Catalog and the Doubleday advance; Steve Jobs's 2005 Stanford invocation; the Kaczynski-cabin reading (did he own or use it? verify) and Fred Turner's account"),
 "douglas_engelbart": ("Douglas C. Engelbart", "person (computer scientist, SRI)",
  "the Augmentation Research Center, the 1968 demo Brand helped film, ARPA and Air Force funding",
  "'Augmenting Human Intellect' (1962), the mouse, NLS, the Dec 9 1968 demo and its crew, ARPA/IPTO (Licklider, Taylor) and Air Force Office of Scientific Research funding, NASA money, the ARPANET's second node, the Erhard Seminars Training (est) episode at ARC, the transfer to Tymshare and McDonnell Douglas, the Bootstrap Institute, the 1997 Turing Award; his own statements on Bush's 'As We May Think'; Thierry Bardini's 'Bootstrapping' (2000); Andreessen's naming of him as influence"),
 "augmentation_research_center": ("Augmentation Research Center (SRI, 1963-77)", "institution/program",
  "Engelbart's lab: military-funded origin of the personal computing interface",
  "SRI's relation to Stanford and its defense contracts (the 1969-70 student protests and the split from Stanford), ARC's funding history by agency and dollar figure, staff (Bill English, Jeff Rulifson, Charles Irby), the 1968 demo, the ARPANET NIC, the est episode, the sale to Tymshare 1977; who from ARC went to Xerox PARC"),
 "darpa": ("ARPA/DARPA (Advanced Research Projects Agency)", "institution",
  "funder of Engelbart, the ARPANET, and the personal computing lineage the video traces",
  "founding 1958 after Sputnik, IPTO under Licklider (1962), Sutherland, Taylor and Roberts, the ARPANET (1969), funding of SRI, MIT Project MAC, Stanford AI Lab, the Mansfield Amendment (1973), the 1996 rename history, later programs relevant to the network (Total Information Awareness 2002 and its dissolution, Palantir's In-Q-Tel and intelligence customers as contrast); the standard histories (Waldrop, Abbate, Hafner and Lyon) and the funding figures"),
 "bill_joy": ("Bill Joy", "person (computer scientist, Sun Microsystems co-founder)",
  "interviewed in 'The Net'; 'Why the Future Doesn't Need Us' (Wired, April 2000) quoted Kaczynski",
  "BSD Unix at Berkeley, vi, Sun (1982), Java, the 2000 Wired essay and its citation of Kaczynski's manifesto via Kurzweil's 'Age of Spiritual Machines', the responses (Brockman's Edge debate), Kleiner Perkins partnership 2005-, the greentech portfolio, his appearance in Dammbeck's film"),
 "john_markoff": ("John Markoff", "person (technology journalist, New York Times)",
  "interviewed in 'The Net'; the reporter who covered Kaczynski's targets and wrote Brand's biography",
  "'Cyberpunk' (1991), 'Takedown' (1996, Mitnick), 'What the Dormouse Said' (2005) on the counterculture and the PC, 'Whole Earth: The Many Lives of Stewart Brand' (2022), his Times coverage of the Unabomber and of Gelernter, his profiles of people Kaczynski targeted (the film's claim: verify who), his own statements in the film"),

 # --- Brockman, Edge, the third culture ---
 "john_brockman": ("John Brockman", "person (literary agent, Edge Foundation founder)",
  "the broker: connected scientists to publishers and capital; introduced Epstein to Gelernter (Dec 2009), Clark and Cappafello (Mar 2011); proposed selling Brockman Inc. to a sovereign fund (2018)",
  "1960s Expanded Cinema Festival and happenings with USCO and Rauschenberg, 'By the Late John Brockman' (1969), the Reality Club (1981), Brockman Inc. and its scientist clients, 'The Third Culture' (1995), Edge Foundation (1996) and its Annual Question, the Billionaires' Dinner at TED, Edge's IRS Form 990 filings with Epstein's gifts ($25,000 Schedule B 2001; totals through 2015 as reported by Evgeny Morozov in The New Republic 2019 and others), the 2004 dinner with Brand and Epstein per the Edge archive, the Edge of Computation Prize 2005, 2011 and 2018 emails from the House Oversight and 2026 releases (the 'dinner with my girls' message, the sovereign-fund proposal, the 'dozen one-year-olds' message and the family's explanation), the collapse of Edge's Question in 2018/19, the Epstein-era resignations; his wife Katinka Matson, his son Max Brockman; his own statements"),
 "edge_foundation": ("Edge Foundation, Inc.", "institution",
  "the venue where Epstein's money and Brockman's scientists met",
  "incorporation 1996, officers (Brockman, Matson), the 990s year by year with Epstein-related contributions and their share of revenue, the Billionaires' Dinners and guest lists as published on Edge, the Edge Master Classes (2007-11, at Epstein-linked venues?), the Annual Question and its contributors, the Reality Club lineage, what closed in 2018-19 and why, the reporting by Morozov, Buzzfeed, and the House Oversight documents; every named scientist who received Epstein money through or beside Edge"),
 "brockman_inc": ("Brockman, Inc.", "institution (literary agency)",
  "the commercial engine: scientist-authors to publishers; the 2018 proposal to sell it to a Middle Eastern sovereign fund via Epstein",
  "founding 1973, the client list and the advances that made popular science a market (Dawkins, Pinker, Dennett, Gelernter, Kurzweil), Katinka Matson and Max Brockman, the 2018 email about a sovereign-fund acquisition (which fund, what Epstein's role was), the agency after 2019"),
 "daniel_dennett": ("Daniel C. Dennett", "person (philosopher)",
  "on the 2002 Epstein flight to TED with Dawkins and Pinker; Edge regular",
  "Tufts, 'Consciousness Explained', 'Darwin's Dangerous Idea', the Brockman/Edge relationship, the 2002 flight documented in the New York Magazine profile and in flight logs, later statements about Epstein, death 2024"),
 "steven_pinker": ("Steven Pinker", "person (psychologist, Harvard)",
  "the 2002 flight to TED; the 2007 Dershowitz letter episode; Edge regular",
  "MIT and Harvard career, Brockman as agent, the 2002 flight, the 2011 Edge photograph and the 2014 St Thomas conference, his linguistic opinion used by Alan Dershowitz in Epstein's 2007 defense and his 2019 statements, the Harvard Program for Evolutionary Dynamics adjacency; distinguish documented from insinuated"),
 "martin_nowak": ("Martin A. Nowak", "person (mathematical biologist, Harvard)",
  "Epstein's $6.5 million gift funded his Program for Evolutionary Dynamics (2003); Harvard's 2020 review sanctioned him",
  "Oxford, IAS Princeton, the 2003 gift and the PED, Epstein's office and key card at the PED, the visits after 2008, Harvard's May 2020 report (Diane Lopez) and the sanctions (two-year bar on advising, closure of PED), his 'SuperCooperators' (2011, with Highfield), the Templeton money; sources: Harvard report, Harvard Crimson, Boston Globe"),
 "stephen_kosslyn": ("Stephen M. Kosslyn", "person (cognitive psychologist, Harvard)",
  "Epstein funded his Harvard laboratory research on mental imagery (New York Magazine 2002)",
  "mental-imagery research, Harvard department chair and dean of social science, the Epstein gifts to his lab with amounts and years (Harvard's 2020 report), his role in Epstein's Harvard visiting-fellow appointment (2005) per the report, his later career at Minerva and Foundry College; his statements"),
 "danny_hillis": ("W. Daniel (Danny) Hillis", "person (computer scientist, inventor)",
  "named in the 2002 profile of Epstein's scientific circle; co-founder of Long Now with Brand",
  "MIT and Thinking Machines (Connection Machine, DARPA funding), Disney Imagineering, Applied Minds, Long Now and the 10,000-year clock (Bezos's funding of the clock), Metaweb/Freebase (sold to Google), Applied Invention; the Epstein connection: what the 2002 article and later reporting document (Edge dinners, the 2011 photograph?) and his own statements"),
 "gerald_edelman": ("Gerald M. Edelman", "person (biologist, Nobel 1972, Neurosciences Institute)",
  "Epstein visited his Neurosciences Institute asking whether the brain is a computer (2002 profile)",
  "antibody structure Nobel, Rockefeller University, the Neurosciences Institute (1981, La Jolla from 1993) and its funders, neural Darwinism, 'Bright Air, Brilliant Fire'; the Epstein visit and any funding documented; death 2014"),
 "long_now_foundation": ("The Long Now Foundation", "institution",
  "Brand and Hillis's foundation; a hub of the same network (Bezos's clock, Rose, Kelly, Eno)",
  "founding 1996 (Brand, Hillis, Kevin Kelly, Brian Eno, Esther Dyson, Mitch Kapor, Peter Schwartz, Paul Saffo), the Clock of the Long Now and Jeff Bezos's $42 million funding on his Texas land, the Rosetta Project, Long Bets, the Interval, revenue and donors from the 990s, the board over time; ties to Global Business Network and Edge"),

 # --- the 2003 reporting and the accusers ---
 "vicky_ward": ("Vicky Ward", "person (journalist)",
  "'The Talented Mr. Epstein', Vanity Fair, March 2003; the Farmer sisters' allegations cut before publication",
  "her account of Epstein's pressure and threats during her pregnancy (2015 Daily Beast essay, 2019 podcast 'Chasing Ghislaine'), Graydon Carter's contrary account, the Farmer sisters' testimony about what they told her, the 2003 article's actual content, her later work; the dispute presented with both versions dated"),
 "graydon_carter": ("Graydon Carter", "person (editor, Vanity Fair 1992-2017)",
  "disputes Ward's account of why the Farmer allegations were removed",
  "Spy magazine, the Vanity Fair editorship, his statements on the 2003 Epstein piece (legal standard versus Epstein's pressure; the alleged cat's head and bullet delivered to his home per Ward and per John Connolly), his 2025 memoir 'When the Going Was Good'; every version dated and sourced"),
 "maria_farmer": ("Maria Farmer", "person (artist; first known Epstein accuser to law enforcement, 1996)",
  "went on record to Vicky Ward in 2002-3 with Annie; the allegations were removed",
  "her 1996 FBI and NYPD reports, work for Epstein at the New York mansion and the Wexner Ohio estate (Les Wexner's role), the 2019 sworn affidavit, her 2019 lawsuit against the Epstein estate and Ghislaine Maxwell, her interviews (CBS, Whitney Webb), her account of Ward and Vanity Fair; the FBI's 1996 inaction as documented in the DOJ OPR record"),
 "annie_farmer": ("Annie Farmer", "person (psychologist; Epstein accuser, New Mexico 1996)",
  "the sister who also spoke to Ward in 2002-3; testified at Maxwell's 2021 trial",
  "the 1996 Zorro Ranch episode at sixteen, her testimony at the 2019 bail hearing and the Maxwell trial (Dec 2021), the Vanity Fair episode, her 2019 lawsuit, the Epstein Victims' Compensation Program"),

 # --- the later network: Silicon Valley, AI, Palantir ---
 "eric_schmidt": ("Eric Schmidt", "person (Google CEO 2001-11, chairman; investor)",
  "Brockman dinner guest; dated Kammie/Cammie Clark c. 2011; joined Anthropic's 2021 financing",
  "Sun and Novell, Google, Alphabet, the Schmidt Futures and Schmidt Sciences philanthropy, the Defense Innovation Board and National Security Commission on AI, the 2021 Anthropic Series A participation (verify amounts), his personal relationships as reported (Clark; the Manhattan penthouse reporting), any Epstein contact documented in the released files (verify: the 2026 release), Brockman dinners; the Special Competitive Studies Project"),
 "dario_amodei": ("Dario Amodei", "person (AI researcher, Anthropic co-founder and CEO)",
  "married Clark in 2022; the video's furthest downstream node, with its own disclaimer that no Anthropic-Epstein relationship is established",
  "Princeton physics and Stanford biophysics, Baidu, Google Brain, OpenAI (GPT-2, GPT-3, scaling laws), the 2021 Anthropic founding with Daniela Amodei and others, the funding rounds (Schmidt in Series A, Google, Spark, FTX/Alameda's $500 million, Amazon), 'Machines of Loving Grace' (2024); the marriage as reported; state plainly what the record does not show"),
 "cammie_clark": ("Cammie (Kamie) Clark", "person (media entrepreneur; married Dario Amodei 2022)",
  "introduced to Epstein by Brockman in March 2011 ('dinner with my girls'); pitched a company to Epstein; formerly dating Eric Schmidt",
  "SPELLING UNVERIFIED: the name is transcribed from audio as 'Cammie Clark' and her companion as 'Michelle Cappafello'; establish the correct names from the released documents first. Then: the 2011 emails (Brockman's introduction, her replies, the funding request, the company's nature per the documents), the reported Schmidt relationship, the 2014 relationship and 2022 marriage with Amodei, her role in bringing Schmidt into Amodei's orbit as claimed; also cover Michelle Cappafello (spelling unverified) inside this dossier as the second person introduced. Living private individual: primary documents and named reporting only, every claim tiered"),
 "jeff_bezos": ("Jeff Bezos", "person (Amazon founder)",
  "Brockman billionaire-dinner guest; funder of the Long Now clock; Amazon's Anthropic investment",
  "Amazon, Blue Origin, Washington Post, the Long Now clock funding, Edge dinner appearances with dates, any Epstein contact in the record (verify), the 2023-24 Amazon investment in Anthropic ($4 billion); keep the network section to documented ties"),
 "sergey_brin": ("Sergey Brin", "person (Google co-founder)",
  "Brockman dinner guest",
  "Google's founding, Alphabet, the Brin Wojcicki Foundation, Edge dinner appearances with dates, any documented Epstein or Brockman ties, his 2020s AI return"),
 "larry_page": ("Larry Page", "person (Google co-founder)",
  "Brockman dinner guest",
  "Google, Alphabet, Kitty Hawk, Edge dinner appearances with dates, documented ties only"),
 "melinda_french_gates": ("Melinda French Gates", "person (philanthropist)",
  "named with Bill Gates on the Brockman dinner guest list; her stated objection to Gates's Epstein meetings",
  "Microsoft, the Gates Foundation, the Edge dinner appearances, her 2022 statements on Epstein as a factor in the divorce, Pivotal Ventures; documented ties only"),
 "palantir_technologies": ("Palantir Technologies", "institution/company",
  "founded 2003, the year of 'The Net'; the map made machine",
  "founding (Thiel, Karp, Cohen, Lonsdale, Gettings), In-Q-Tel's investment and the CIA as first customer, PayPal fraud-detection origins, Gotham and Foundry, the ICE, NHS, Army and NSA contracts with figures, the 2020 direct listing, Project Maven, the 2025 'Technological Republic' and the April 2026 22-point X thread (verify text), the ImmigrationOS reporting, the Cambridge Analytica employee episode, TITAN; revenue and government share by year"),
 "dialog_thiel_network": ("Dialog (Thiel's invitation-only conference network)", "institution/event",
  "the leaked records claiming it collected romantic preferences and matchmade members",
  "founding (2015? with Auren Hoffman; verify), the Dialog Foundation, Dialog Weekend, the leak reported in 2025-26 (which outlet, what documents), attendees, Thiel's funding, the matchmaking function as documented versus as alleged; compare Edge dinners"),
 "nicholas_zamiska": ("Nicholas W. Zamiska", "person (Palantir head of corporate affairs, co-author)",
  "co-author with Alex Karp of 'The Technological Republic' (2025)",
  "Wall Street Journal Asia reporting career, Yale Law, Palantir role since 2014, the book's argument and reception, the 22-point summary of April 2026"),
 "the_technological_republic": ("The Technological Republic: Hard Power, Soft Belief, and the Future of the West (Karp and Zamiska, 2025)", "text",
  "the argument that Silicon Valley's engineers owe national defense their participation",
  "publication, argument chapter by chapter, reception (reviews in NYT, FT, Guardian, the critical essays), the April 2026 22-point X post, the relation to Andreessen's manifesto and to Kaczynski's thesis as the video frames it"),
 "techno_optimist_manifesto": ("The Techno-Optimist Manifesto (Marc Andreessen, October 2023)", "text",
  "the 'photographic negative' of Kaczynski's manifesto; its list of 'patron saints' names von Neumann, Engelbart, Brand, Land",
  "the text, its enemies list, the full patron-saint list with each name, reception and critiques, the Effective Accelerationism (e/acc) context, its relation to Land's accelerationism and to the Andreessen Horowitz portfolio"),
 "industrial_society_and_its_future": ("Industrial Society and Its Future (the Unabomber manifesto, 1995)", "text",
  "the text whose predictions the video tests",
  "the negotiation with the New York Times and Washington Post, the Sept 19 1995 publication, the FBI's decision and Freeh/Reno, the 232 paragraphs and their argument (the power process, oversocialization, technology as choice becoming necessity, convergence, human modification), the sources it drew on (Ellul, Zerzan, Mumford), the linguistic identification, its afterlife in print (Fitch & Madison 2010), online and among ecofascists and 'pine tree' accounts; scholarly assessments"),
 "trilateral_commission": ("Trilateral Commission", "institution",
  "Epstein appears on its 1995 membership roster",
  "founding 1973 (Rockefeller, Brzezinski), membership rules and the published rosters, the 1995 roster with Epstein and how he was listed, the Commission's finances, the conspiracy literature around it (from the 1970s right and left) stated as such; other members relevant to this network"),
 "council_on_foreign_relations": ("Council on Foreign Relations", "institution",
  "Epstein listed as a member 1995-2009 (dates per the roster; verify)",
  "founding 1921, membership process, Epstein's membership years and how it ended, Foreign Affairs, funding, other members in this network; the conspiracy narratives stated as such"),
 "program_for_evolutionary_dynamics": ("Program for Evolutionary Dynamics (Harvard, 2003-2020)", "institution/program",
  "founded with Epstein's $6.5 million; Epstein had an office and campus access there after 2008",
  "the 2003 gift and its terms, Nowak's directorship, Epstein's office, key card and visits (over forty after 2008 per Harvard's report), the Harvard 2020 review and its findings and sanctions, the program's closure, publications and people funded"),
}

# order: run everything; put the heaviest network hubs first so they land early
ORDER = [
 "john_brockman", "edge_foundation", "david_gelernter", "theodore_kaczynski", "stewart_brand",
 "lutz_dammbeck", "the_net_film_2003", "henry_murray", "murray_harvard_experiment", "mkultra",
 "macy_conferences", "warren_mcculloch", "margaret_mead", "gregory_bateson", "heinz_von_foerster",
 "marshall_mcluhan", "robert_rauschenberg", "arthur_k_solomon", "whole_earth_catalog",
 "douglas_engelbart", "augmentation_research_center", "darpa", "bill_joy", "john_markoff",
 "brockman_inc", "daniel_dennett", "steven_pinker", "martin_nowak", "stephen_kosslyn", "danny_hillis",
 "gerald_edelman", "long_now_foundation", "program_for_evolutionary_dynamics",
 "vicky_ward", "graydon_carter", "maria_farmer", "annie_farmer",
 "eric_schmidt", "dario_amodei", "cammie_clark", "jeff_bezos", "sergey_brin", "larry_page",
 "melinda_french_gates", "palantir_technologies", "dialog_thiel_network", "nicholas_zamiska",
 "the_technological_republic", "techno_optimist_manifesto", "industrial_society_and_its_future",
 "trilateral_commission", "council_on_foreign_relations",
 "charles_epstein_geneticist", "joel_gelernter", "james_mcconnell", "nicklaus_suino", "hugh_scrutton",
 "thomas_mosser", "gilbert_murray_forester", "richard_j_roberts", "phillip_sharp",
 "david_kaczynski", "linda_patrik",
]
assert set(ORDER) == set(SIGNS), set(ORDER) ^ set(SIGNS)

if __name__ == "__main__":
    for slug, (name, klass, role, pointers) in SIGNS.items():
        text = f"""# {name}: research brief

Cybernetic-elite research, Anthony 2026-09-28, separate from the atlas. Appended to
PROMPT_TEMPLATE_CYBERNETIC_ELITE.md by tools/codex_dossier_set.py.

---

SUBJECT. {name}. Class: {klass}.

PLACE IN THE NETWORK (as the video "The Unabomber & the Net: Kaczynski, Epstein and the Cybernetic
Elite", Hidden AmuraKa 2026, frames it; verify or refute, never repeat unexamined): {role}.

THREADS TO PULL, each verified against primary sources and dated: {pointers}.

THE NETWORK SECTION is the deliverable that matters most for this set: every documented tie to any
other named person, institution, fund, agency, company or program, one line each with date, source
and evidence tier, so that the ties can be assembled into a map across the whole set. Name the
other party exactly (full names, no bare surnames). Where the video asserts a tie, say whether the
record supports it.

STANCE. Rumor as fully as fact, never rumor as fact. Living subjects and litigated claims: name
the source and the tier for every accusation. Absence of evidence is a finding: say what could not
be traced.
"""
        open(os.path.join(OUT, f"{slug}.brief.md"), "w").write(text)
        print("wrote", slug)
