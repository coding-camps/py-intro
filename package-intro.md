
------------------------------------------------------------------------------------------

> https://www.python.org/about/apps/

# Applications for Python


Python is used in many application domains. Here's a sampling.

The [Python Package Index](http://pypi.org/) lists thousands of third party modules for Python.

## Web and Internet Development

Python offers many choices for [web development](http://wiki.python.org/moin/WebProgramming):

- Frameworks such as [Django](http://www.djangoproject.com/) and [Pyramid](http://www.pylonsproject.org/).
- Micro-frameworks such as [Flask](http://flask.pocoo.org/) and [Bottle](http://bottlepy.org/).
- Advanced content management systems such as [Plone](http://www.plone.org/) and [django CMS](https://www.django-cms.org/).

Python's standard library supports many Internet protocols:

- [HTML and XML](http://docs.python.org/library/markup)
- [JSON](http://docs.python.org/library/json.html)
- [E-mail processing](http://docs.python.org/library/email).
- Support for [FTP](http://docs.python.org/library/ftplib.html), [IMAP](http://docs.python.org/2/library/imaplib.html), and other [Internet protocols](http://docs.python.org/library/internet).
- Easy-to-use [socket interface](http://docs.python.org/howto/sockets.html).

And the Package Index has yet more libraries:

- [Requests](https://pypi.org/project/requests/), a powerful HTTP client library.
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/), an HTML parser that can handle all sorts of oddball HTML.
- [Feedparser](https://pypi.org/project/feedparser/) for parsing RSS/Atom feeds.
- [Paramiko](https://pypi.org/project/paramiko/), implementing the SSH2 protocol.
- [Twisted Python](http://twistedmatrix.com/), a framework for asynchronous network programming.

## Scientific and Numeric

Python is widely used in [scientific and numeric](http://wiki.python.org/moin/NumericAndScientific) computing:

- [SciPy](http://scipy.org/) is a collection of packages for mathematics, science, and engineering.
- [Pandas](http://pandas.pydata.org/) is a data analysis and modeling library.
- [IPython](http://ipython.org/) is a powerful interactive shell that features easy editing and recording of a work session, and supports visualizations and parallel computing.
- The [Software Carpentry Course](http://software-carpentry.org/) teaches basic skills for scientific computing, running bootcamps and providing open-access teaching materials.

## Education
Python is a superb language for teaching programming, both at the introductory level and in more advanced courses.

- Books such as [How to Think Like a Computer Scientist](http://www.openbookproject.net/thinkcs/python/english2e/), [Python Programming: An Introduction to Computer Science](http://mcsp.wartburg.edu/zelle/python/), and [Practical Programming](http://pragprog.com/book/gwpy2/practical-programming).

- The [Education Special Interest Group](https://www.python.org/community/sigs/current/edu-sig) is a good place to discuss teaching issues.


## Desktop GUIs

The [Tk](http://wiki.python.org/moin/TkInter) GUI library is included with most binary distributions of Python.

Some toolkits that are usable on several platforms are available separately:

- [wxWidgets](http://www.wxpython.org/)
- [Kivy](http://kivy.org/), for writing multitouch applications.
- Qt via [pyqt](http://www.riverbankcomputing.co.uk/software/pyqt/intro) or [pyside](http://www.pyside.org/)

Platform-specific toolkits are also available:

- [GTK+](http://www.pygtk.org/)
- Microsoft Foundation Classes through the [win32 extensions](http://sourceforge.net/projects/pywin32/)


## Software Development

Python is often used as a support language for software developers, for build control and management, testing, and in many other ways.

- [SCons](http://www.scons.org/) for build control.
- [Buildbot](http://buildbot.sourceforge.net/) and [Apache Gump](http://gump.apache.org/) for automated continuous compilation and testing.
- [Roundup](https://roundup.sourceforge.net/) or [Trac](https://trac.edgewall.org/) for bug tracking and project management.

## Business Applications

Python is also used to build ERP and e-commerce systems:

- [Odoo](https://www.odoo.com/) is an all-in-one management software that offers a range of business applications that form a complete suite of enterprise management applications.
- [Tryton](http://www.tryton.org/) is a three-tier high-level general purpose application platform.


------------------------------------------------------------------------------------------

> Page: https://wiki.python.org/moin/NumericAndScientific

## Numeric and Scientific

- NumPy - http://www.numpy.org/ -- Numerical Python adds a fast, compact, multidimensional array facility to Python. NumPy is the successor to both Numeric and Numarray.

  - Deprecated: Numeric -- Numerical Python adds a fast, compact, multidimensional array language facility to Python. (Note: superseded by NumPy)

  - Deprecated: NumArray - http://stsdas.stsci.edu/numarray/index.html -- Numarray is a reimplementation of Numeric which adds the ability to efficiently manipulate large numeric arrays in ways similar to Matlab and IDL. (Note: superseded by NumPy)

- SciPy - http://www.scipy.org/ SciPy is an open source library of scientific tools for Python. SciPy supplements the popular NumPy module, gathering a variety of high level science and engineering modules together as a single package. SciPy includes modules for linear algebra, optimization, integration, special functions, signal and image processing, statistics, genetic algorithms, ODE solvers, and others.

- Numba - http://numba.pydata.org/ Numba is an open source, NumPy-aware Python compiler specifically suited to scientific codes.

- [ad](http://pypi.python.org/pypi/ad) is an open-source Python package for transparently performing first- and second-order automatic differentiation calculations with any of the base numeric types (int, float, complex, etc.). Utility functions designed for working with SciPy optimization routines.

- APM Python - http://apmonitor.com/wiki/index.php/Main/PythonApp APMonitor is a nonlinear programming and optimization environment with an interface to Python. The software is available as a web-service through Python libraries for the solution of large-scale mathematical programming problems.

- SymPy - http://www.sympy.org/ SymPy is a symbolic manipulation package, written in pure Python. Its aim is to become a full featured CAS in Python, while keeping the code as simple as possible in order to be comprehensible and easily extensible.

- ALGLIB - http://www.alglib.net/ - numerical analysis library in C++ and C#, with Python and IronPython interfaces.

- Python Data Analysis Library - http://pandas.pydata.org/ - pandas is a library providing high-performance, easy-to-use data structures and data analysis tools for the Python .

- PyGSL - http://pygsl.sourceforge.net/ -- This project provides a python interface for the GNU scientific library (gsl).

- FuncDesigner - http://openopt.org/FuncDesigner FuncDesigner is Python module to rapidly build functions and get their derivatives via automatic differentiation. Also you can perform integration, interpolation, interval analysis, uncertainty analysis, solve eigenvalue problems, systems of linear/non-linear/ODE equations and numerical optimization problems coded in FuncDesigner by OpenOpt.

- OpenOpt - http://openopt.org - a framework for numerical optimization and systems of linear/non-linear equations. Connects to dozens of solvers (some are C- or Fortran-written). Can optimize FuncDesigner models with automatic differentiation. Provides graphic output of convergence, multifactor analysis tool for scientific experiments planning and some more numerical optimization "MUST HAVE" features. Also OpenOpt has Stochastic Programming and Optimization addon (commercial yet, free for small-scaled academic and research purposes)

- SpaceFuncs - http://openopt.org/SpaceFuncs - a tool for 2D, 3D, N-dimensional geometric modeling with possibilities of parametrized calculations, numerical optimization and solving systems of geometrical equations with automatic differentiation.

- !NLopt - http://ab-initio.mit.edu/nlopt - another library for nonlinear optimization, including many local/global optimization algorithms written in C, with a Python interface (as well as interfaces for several other languages).

- jHepWork - http://jwork.org/jhepwork - a multiplatform data-analysis framework written in Java. The main programming language is Jython, a clone of Python written in Java. Contains Java libraries for numerical calculations and visualisation of scientific graphs. Contains an interactive Python prompt.

- ScientificPython - http://dirac.cnrs-orleans.fr/ScientificPython/ -- ScientificPython is a collection of Python modules that are useful for scientific computing. In this collection you will find modules that cover basic geometry (vectors, tensors, transformations, vector and tensor fields), quaternions, automatic derivatives, (linear) interpolation, polynomials, elementary statistics, nonlinear least-squares fits, unit calculations, Fortran-compatible text formatting, 3D visualization via VRML, and two Tk widgets for simple line plots and 3D wireframe models. There are also interfaces to the netCDF library (portable structured binary files), to MPI (Message Passing Interface, message-based parallel programming), and to BSPlib (Bulk Synchronous Parallel programming).

- PyACTS- http://wiki.python.org/moin/PyACTS -- PyACTS is a collection of Python Modules that are very useful to Parallel Computing in a High Performance Computing environment. This packages incorporates several modules like PyBLACS (allows communication data for Linear Algebra), PyPBLAS (distributed Matrix Operations) and PyScaLAPACK (solve linear systems and get the eigenvalue problems). These libraries are part of PyACTS project that provide interfaces to the ACTS Collection. Also is provided a parallel interpreter for using this package that implements message-based parallel programming using MPI.

- PyDSTool - http://pydstool.sourceforge.net -- PyDSTool is an integrated simulation, modeling and analysis package for dynamical systems (including ODEs, DAEs, maps, and hybrid systems) and scientific data. Building on SciPy classes, the package also supports symbolic expression processing, bifurcation analysis, and enhanced arrays for "index-free" and highly contextualized scientific data manipulation. Model building tools use symbolic expression and hierarchical specification classes to ease the development and analysis of complex models. This includes automated compilation of symbolic representations of models into fast numerical code using enhanced legacy Fortran and C integrators for both stiff and non-stiff systems.

- escript - https://launchpad.net/escript-finley -- escript is a Python module to define and solve coupled, non-linear, time-dependent partial differential equations (PDEs). The user has to implement high-level time integration schemes and iteration schemes to reduce the problem to the solution of steady, linear systems of PDEs which are solved by a suitable PDE solver library. The current version uses the FEM solver library finley but the design is open and other libraries can be used. escript is parallelized for OpenMP and MPI. It is compatible with NumPy and VTK for visualization.

- PyIMSL - http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx -- PyIMSL is a collection of Python wrappers to the mathematical and statistical algorithms in the IMSL C Numerical Library. PyIMSL offers a quality Python interface to the largest collection of portable statistical and analytical algorithms available for Python. Developers can use Python, PyIMSL and the IMSL C Library for rapid prototyping. They can then directly deploy the Python application into production or if they choose to rewrite the application in C/C++ use the same math and stats algorithms in both development environments. PyIMSL Studio is a packaged, supported and documented development environment designed for deploying mathematics and statistics prototype models into production applications. PyIMSL Studio includes the Python language distribution and contains both open source and proprietary components that create a fully supported and documented platform for analytic prototyping and production development. PyIMSL Studio is available for download at no charge for non-commercial use or for commercial evaluation.

- PyGTS - http://pygts.sourceforge.net/ -- PyGTS is a python package used to construct, manipulate, and perform computations on 3D triangulated surfaces. It is a hand-crafted and pythonic binding for the GNU Triangulated Surface (GTS) Library (http://gts.sourceforge.net/).

- scikit-learn - http://scikit-learn.sourceforge.net/ -- machine learning and data mining in Python, using NumPy and SciPy

- mlpy - https://mlpy.fbk.eu/ -- Machine Learning PYthon -- high-performance Python module for Predictive Modeling.

- graph-tool - http://graph-tool.skewed.de -- A python module for efficient analysis of graphs (aka. networks), with algorithms implemented in C++ with the Boost Graph Library.

- sppy - http://packages.python.org/sppy/index.html -- A sparse matrix package based on Eigen.

- Quandl - https://www.quandl.com/tools/python -- An API package to access http://quandl.com datasets, as well as upload data to Quandl.


## Multi precision math


- MultiprecisionSoftwareDirectory (http://crd.lbl.gov/~dhbailey/mpdist/index.html) - Python wrapping unknown

- MAPM (http://www.tc.umn.edu/~ringx004/mapm-main.html) - Python wrapping unknown

- GmPy (http://gmpy.sourceforge.net/) - GNU Multiple Precision library wrapping

- mpmath - http://mpmath.org/ - mpmath is a pure Python library for arbitrary-precision floating-point arithmetic, with support for complex numbers. Implements all the transcendental functions from Python's math and cmath modules and many others.

- clnum - http://calcrpnpy.sourceforge.net/clnum.html - Class Library For Numbers wrapping

## The Grid

Grid is a type of parallel and distributed system that enables the sharing, selection, and aggregation of resources distributed across "multiple" administrative domains based on their (resources) availability, capability, performance, cost, and users' quality-of-service requirements.

- PyGlobus - Globus toolkit bindings for python

- PEG - Python Extensions for the Grid

- Ganga - Grid job management interface.

- DIANE - Python user-level middleware layer for Grids.

## Geographic Information System (GIS), Mapping, Image Processing and Analysis

- Thuban is a Python Interactive Geographic Data Viewer with the following features:

    - Vector Data Support: Shapefile, PostGIS Layer, Raster Data Support: GeoTIFF Layer, Comfortable Map Navigation, Object Identification and Annotation, Legend Editor and Classification, Table Queries and Joins, Projection Support, Printing and Vector Export, API for Add-Ons (Extensions), Multi-Language Support: English, French, German, Hungarian, Italian, Russian and Spanish, User Manual (English) Multi-platform (GNU/Linux, Windows, ...). (Noli Sicad)

- Python Cartographic Library, OWSLib, GeoJSON, and Rtree - packages for GIS programming and a cartographic application framework.

- PySAL Python Spatial Analysis LIbrary - an open source cross-platform library of spatial analysis functions written in Python. It is intended to support the development of high level applications for spatial analysis.

- sDNA is freeware spatial network analysis software developed by Cardiff university, and has a Python API.

## Image analysis and visualization

- Bokeh - http://bokeh.pydata.org/ - is a Python interactive visualization library for large datasets that natively uses the latest web technologies.

- scikit-image - **http://scikit-image.org/** - is an image processing library written in Python/Cython for use with NumPy and SciPy

- VTK - http://vtk.org/ - is an open source, freely available software system for 3D computer graphics, image processing, and visualization used by thousands of researchers and developers around the world. It has a very good python interface.

- WrapITK - http://code.google.com/p/wrapitk/ - interface ITK http://itk.org and several languages, with a particular focus on python. ITK module used with python interpreter is particulary useful for quick and easy prototyping of image analysis procedures. Some glue classes allow to efficiently pass data to others modules like NumPy or VTK.

- PIL - http://www.pythonware.com/products/pil - Python Imaging Library provides basic image handling and processing for various image types including jpg, gif, tiff, and bmp. Reads and writes graphics files. Allows pixel-by-pixel data access and has functions for cropping and transposing an image. Also has various filters built-in.

- matplotlib - http://matplotlib.sourceforge.net/ - matplotlib is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell (ala matlab or mathematica), web application servers, and six graphical user interface toolkits.

- GR Framework - http://gr-framework.org/ - GR is a universal framework for cross-platform visualization applications. It offers developers a compact, portable and consistent graphics library for their programs. Applications range from publication quality 2D graphs to the representation of complex 3D scenes. GR can be used in imperative programming systems or integrated into modern object-oriented systems, in particular those based on GUI toolkits. The GR framework is especially suitable for real-time environments.

- Plotly - https://plot.ly/- is a collaborative graphing and analytics platform. The web app has an online Python sandbox - NumPy supported - and grid for data analysis. The Plotly graphing library produces graphs that are interactive, publication quality, and browser-based. Graphs can be styled with Python or a GUI, shared, embedded, and exported.

- Mayavi - http://code.enthought.com/projects/mayavi/ - application and library for interactive visualization in 3D of scientific data. High level and targeted toward the end user/application developer.

- VisTrails - http://vistrails.org - VisTrails is an open-source scientific workflow and provenance management system developed at the University of Utah that provides support for data exploration and visualization.

- Glumpy - http://glumpy.github.io/ - a small python library that uses OpenGL for the rapid vizualization of (mainly two dimensional) numpy arrays. Not so much for nice figures for inclusion in a scientific article, more for rapid vizualization of your running simulation.

- pyqtgraph - http://luke.campagnola.me/code/pyqtgraph/ - Pure-python graphics and GUI library for scientific/angineering applications based on PyQt and numpy. This library provides fast plotting and image/video display, multidimensional image slicing, volumetric / isosurface rendering, interactive data manipulation tools, and a variety of Qt widgets including an editable property tree, visual programming flowchart, and gradient editor.


## Life sciences

- Biopython - http://biopython.org/wiki/Main_Page -- a set of freely available tools for biological computation and bioinformatics. It includes pycluster, a binding for the Cluster software.

- PyCogent - http://pycogent.sourceforge.net/ -- COmparative GENomic Toolkit. Another popular and extensive library for genomic biology.

- track - http://xapple.github.com/track/ -- Provides easy read/write access to genomic tracks in a fashion that is independent from the underlying format. Implemented formats include: BED; WIG; GFF; GTF; BedGraph; BigWig.

- PyChem - http://pychem.sf.net/ -- a cross-platform open source package for multivariate analysis, that includes a graphical user interface.

- bx-python - http://bitbucket.org/james_taylor/bx-python/ -- Library and associated set of scripts to allow for rapid implementation of genome scale-analyses. Also a fundamental part of the ongoing Galaxy and ESPERR projects.

- p4 - http://bmnh.org/~pf/p4.html -- Python package for phylogenetics, useful for programmatic manipulation of phylogenetic data and trees, including maximum likelihood and Bayesian inference.

- UCSF Chimera - http://www.cgl.ucsf.edu/chimera/ -- UCSF Chimera is a highly extensible program for interactive visualization and analysis of molecular structures and related data, including density maps, supramolecular assemblies, sequence alignments, docking results, trajectories, and conformational ensembles. High-quality images and animations can be generated. Chimera includes complete documentation and several tutorials, and can be downloaded free of charge for academic, government, non-profit, and personal use.

- Modeller - http://salilab.org/modeller -- used for homology or comparative modeling of protein three-dimensional structures. Control scripts are Python based.

- PyMol - http://www.pymol.org/ -- 3D molecular viewer, suitable (and widely used) for publications and presentations. Fully scriptable in Python.


## Space Sciences

- Astropy aims to develop a single core package for Astronomy in Python and foster interoperability between Python astronomy packages.

- SunPy project is an effort to create an open-source software library for solar physics using Python.

- Spacepy is a set of Python-Based Tools for the Space Science Community.


## Miscellaneous

- PyLink is an open source Python module for interfacing with the EyeLink eye tracking hardware. Find it at PyLink

- SimPy is an open-source discrete-event simulation package in Python. Read more at its Homepage

- uncertainties is an open-source Python package for transparently performing calculations with uncertainties (3.14±0.01…).

- soerp is a free and open-source Python package for quickly and transparently performing calculator-style second-order error propagation (utilizes ad for derivatives).

- mcerp: an open-source real-time, latin-hypercube-based Monte-Carlo alternative to uncertainty/error propagation, but isn't order specific like soerp and uncertainties.

## Links

- NumericAndScientific/Plotting --

- NumericAndScientific/Libraries -- useful libraries

- NumericAndScientific/Formats -- modules for reading and writing various file formats

- NumericBooks

    - CERN ROOT Python Services -- Automatic Python/C/C++ binding

    - Anaconda -- Free distribution with many Scientific Libraries pre-packaged.

    - Numfocus -- Non-profit supporting NumPy stack and accessible computing for science.

------------------------------------------------------------------------------------------

> https://numpy.org/

# Numpy Ecosystem

## Scientific Domains

Nearly every scientist working in Python draws on the power of NumPy.

NumPy brings the computational power of languages like C and Fortran to Python, a language much easier to learn and use. With this power comes simplicity: a solution in NumPy is often clear and elegant.

### Quantum Computing
- QuTiP http://qutip.org/
- PyQuil https://pyquil-docs.rigetti.com/en/stable
- Qiskit https://qiskit.org/
- PennyLane https://pennylane.ai/

### Statistical Computing
- Pandas https://pandas.pydata.org/
- statsmodels https://www.statsmodels.org/
- Xarray https://xarray.pydata.org/en/stable/
- Seaborn https://seaborn.pydata.org/


### Signal Processing 
- SciPy https://www.scipy.org/
- PyWavelets https://pywavelets.readthedocs.io/
- python-control https://python-control.org/
- HyperSpy https://hyperspy.org/

### Image Processing
- Scikit-image https://scikit-image.org/
- OpenCV https://opencv.org/
- Mahotas https://mahotas.rtfd.io/

### Graphs and Networks
- NetworkX https://networkx.org/
- graph-tool https://graph-tool.skewed.de/
- igraph https://igraph.org/python/
- PyGSP https://pygsp.rtfd.io/

### Astronomy
- AstroPy https://www.astropy.org/
- SunPy https://sunpy.org/
- SpacePy https://spacepy.github.io/

### Cognitive Psychology
- PsychoPy https://www.psychopy.org/

### Bioinformatics
- BioPython https://biopython.org/
- Scikit-Bio http://scikit-bio.org/
- PyEnsembl https://github.com/openvax/pyensembl
- ETE http://etetoolkit.org/

### Bayesian Inference
- PyStan https://pystan.readthedocs.io/en/latest/
- PyMC3 https://docs.pymc.io/
- ArviZ https://arviz-devs.github.io/arviz/
- emcee https://emcee.readthedocs.io/

### Mathematical Analysis
- SciPy https://www.scipy.org/
- SymPy https://www.sympy.org/
- cvxpy https://www.cvxpy.org/
- FEniCS https://fenicsproject.org/

### Chemistry
- Cantera https://cantera.org/
- MDAnalysis https://www.mdanalysis.org/
- RDKit https://github.com/rdkit/rdkit
- PyBaMM https://www.pybamm.org/

### Geoscience
- Pangeo https://pangeo.io/
- Simpeg https://simpeg.xyz/
- ObsPy https://github.com/obspy/obspy/wiki
- Fatiando a Terra https://www.fatiando.org/

### Geographic Processing
- Shapely https://shapely.readthedocs.io/
- GeoPandas https://geopandas.org/
- Folium https://python-visualization.github.io/folium

### Architecture & Engineering
- COMPAS https://compas.dev/
- City Energy Analyst https://cityenergyanalyst.com/
- Sverchok https://nortikin.github.io/sverchok/



## Array Libraries

NumPy's API is the starting point when libraries are written to exploit innovative hardware, create specialized array types, or add capabilities beyond what NumPy provides.

- [Dask](https://dask.org/): Distributed arrays and advanced parallelism for analytics, enabling performance at scale.

- [CuPy](https://cupy.dev/): NumPy-compatible array library for GPU-accelerated computing with Python.

- [JAX](https://jax.readthedocs.io/): Composable transformations of NumPy programs: differentiate, vectorize, just-in-time compilation to GPU/TPU.

- [Xarray](https://xarray.pydata.org/en/stable/index.html): Labeled, indexed multi-dimensional arrays for advanced analytics and visualization.

- [Sparse](https://sparse.pydata.org/en/latest/): NumPy-compatible sparse array library that integrates with Dask and SciPy's sparse linear algebra.

- [PyTorch](https://pytorch.org/): Deep learning framework that accelerates the path from research prototyping to production deployment.

- [TensorFlow](https://www.tensorflow.org/): An end-to-end platform for machine learning to easily build and deploy ML powered applications.

- [Arrow](https://arrow.apache.org/): A cross-language development platform for columnar in-memory data and analytics.

- [xtensor](https://github.com/xtensor-stack/xtensor-python): Multi-dimensional arrays with broadcasting and lazy computing for numerical analysis.

- [Awkward Array](https://awkward-array.org/): Manipulate JSON-like data with NumPy-like idioms.

- [uarray](https://uarray.org/en/latest/): Python backend system that decouples API from implementation; unumpy provides a NumPy API.

- [tensorly](http://tensorly.org/stable/home.html): Tensor learning, algebra and backends to seamlessly use NumPy, PyTorch, TensorFlow or CuPy.



## Data Science

NumPy lies at the core of a rich ecosystem of data science libraries. A typical exploratory data science workflow might look like:

### Extract, Transform, Load: 
- [Pandas](https://pandas.pydata.org/), 
- [Intake](https://intake.readthedocs.io/) 
- [PyJanitor](ttps://pyjanitor-devs.github.io/pyjanitor/)

### Exploratory analysis: 
- Jupyter https://jupyter.org/
- Seaborn https://seaborn.pydata.org/
- Matplotlib https://matplotlib.org/
- Altair https://altair-viz.github.io/

### Model and evaluate: 
- scikit-learn https://scikit-learn.org/
- statsmodels https://www.statsmodels.org/stable/index.html
- PyMC3 https://docs.pymc.io/
- spaCy https://spacy.io/

### Report in a dashboard: 
- Dash https://plotly.com/dash
- Panel https://panel.holoviz.org/
- Voila https://voila.readthedocs.io/

For high data volumes, [Dask](https://dask.org/) and [Ray](https://ray.io/) are designed to scale. Stable deployments rely on data versioning ([DVC](https://dvc.org/)), experiment tracking (MLFlow: https://mlflow.org/), and workflow automation ([Airflow](https://airflow.apache.org/), [Dagster](https://dagster.io/) and [Prefect](https://www.prefect.io/)).

## Machine Learning

NumPy forms the basis of powerful machine learning libraries like [scikit-learn](https://scikit-learn.org/) and [SciPy](https://www.scipy.org/). As machine learning grows, so does the list of libraries built on NumPy. [TensorFlow’s](https://www.tensorflow.org/) deep learning capabilities have broad applications — among them speech and image recognition, text-based applications, time-series analysis, and video detection. [PyTorch](https://pytorch.org/), another deep learning library, is popular among researchers in computer vision and natural language processing.

Statistical techniques called [ensemble](https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205) methods such as binning, bagging, stacking, and boosting are among the ML algorithms implemented by tools such as [XGBoost](https://xgboost.readthedocs.io/), [LightGBM](https://lightgbm.readthedocs.io/en/latest/), and [CatBoost](https://catboost.ai/) — one of the fastest inference engines. [Yellowbrick](https://www.scikit-yb.org/en/latest/) and [Eli5](https://eli5.readthedocs.io/en/latest/) offer machine learning visualizations.

- scikit-learn https://scikit-learn.org/
- SciPy https://www.scipy.org/
- TensorFlow https://www.tensorflow.org/
- PyTorch https://pytorch.org/
- XGBoost https://xgboost.readthedocs.io/
- LightGBM https://lightgbm.readthedocs.io/en/latest/
- CatBoost https://catboost.ai/


## Visualization

NumPy is an essential component in the burgeoning [Python visualization landscape](https://pyviz.org/overviews/index.html), which includes 
Matplotlib, Seaborn, Plotly, Altair, Bokeh, Holoviz, Vispy, Napari, and PyVista, to name a few.

NumPy’s accelerated processing of large arrays allows researchers to visualize datasets far larger than native Python could handle.

- Matplotlib https://matplotlib.org/
- Seaborn https://seaborn.pydata.org/
- Plotly https://plot.ly/
- Altair https://altair-viz.github.io/
- Bokeh https://docs.bokeh.org/en/latest/
- Holoviz https://holoviz.org/
- Vispy http://vispy.org/
- Napari https://napari.org/
- PyVista https://docs.pyvista.org/

