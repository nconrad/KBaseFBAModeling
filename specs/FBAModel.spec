/*
@author chenry
*/
module KBaseFBA {
    typedef int bool;
    /*
		Reference to a compound object
		@id subws KBaseBiochem.Biochemistry.compounds.[*].id
	*/
    typedef string compound_ref;
    /*
		Reference to a mapping object
		@id ws KBaseOntology.Mapping
	*/
    typedef string mapping_ref;
    /*
		Template biomass ID
		@id external
	*/
    typedef string templatebiomass_id;
    /*
		Template biomass compound ID
		@id external
	*/
    typedef string templatebiomasscomponent_id;
	/*
		Template reaction ID
		@id external
	*/
    typedef string templatereaction_id;
    /*
		ModelTemplate ID
		@id kb
	*/
    typedef string modeltemplate_id;
    /*
		Reference to a model template
		@id ws KBaseBiochem.Media
	*/
    typedef string media_ref;
    /*
		Reference to a model template
		@id ws KBaseGenomes.Genome
	*/
    typedef string genome_ref;
    /*
		Reference to a model template
		@id ws KBaseFBA.ModelTemplate
	*/
    typedef string template_ref;
    /*
		Reference to an OTU in a metagenome
		@id subws KBaseMetagenomes.Metagenome.otus.[*].id
	*/
    typedef string metagenome_otu_ref;
    /*
		Reference to a metagenome object
		@id ws KBaseMetagenomes.Metagenome
	*/
    typedef string metagenome_ref;
    /*
		Reference to a feature of a genome object
		@id subws KBaseGenomes.Genome.features.[*].id
	*/
    typedef string feature_ref;
	/*
		Reference to a gapgen object
		@id ws KBaseFBA.GapgenFormulation
	*/
    typedef string gapgen_ref;
    /*
		Reference to a FBA object
		@id ws KBaseFBA.FBA
	*/
    typedef string fba_ref;
	/*
		Reference to a gapfilling object
		@id ws KBaseFBA.GapfillingFormulation
	*/
    typedef string gapfill_ref;
	/*
		Reference to a complex object
		@id subws KBaseOntology.Mapping.complexes.[*].id
	*/
    typedef string complex_ref;
	/*
		Reference to a reaction object in a biochemistry
		@id subws KBaseBiochem.Biochemistry.reactions.[*].id
	*/
    typedef string reaction_ref;
    /*
		Reference to a reaction object in a model
		@id subws KBaseFBA.FBAModel.modelreactions.[*].id
	*/
    typedef string modelreaction_ref;
    /*
		Reference to a biomass object in a model
		@id subws KBaseFBA.FBAModel.biomasses.[*].id
	*/
    typedef string biomass_ref;
	/*
		Reference to a compartment object in a model
		@id subws KBaseFBA.FBAModel.modelcompartments.[*].id
	*/
    typedef string modelcompartment_ref;
	/*
		Reference to a compartment object
		@id subws KBaseBiochem.Biochemistry.compartments.[*].id
	*/
    typedef string compartment_ref;
	/*
		Reference to a compound object in a model
		@id subws KBaseFBA.FBAModel.modelcompounds.[*].id
	*/
    typedef string modelcompound_ref;
    /*
		Reference to regulatory model
		@id ws KBaseRegulation.RegModel
	*/
    typedef string regmodel_ref;
    /*
		Reference to PROM model
		@id ws KBaseRegulation.PROMModel
	*/
    typedef string prommodel_ref;
    /*
		Reference to probabilistic annotation
		@id ws KBaseProbabilisticAnnotation.ProbAnno
	*/
    typedef string probanno_ref;
    /*
		Reference to a phenotype set object
		@id ws KBasePhenotypes.PhenotypeSet
	*/
    typedef string phenotypeset_ref;
    /*
		Reference to a phenotype simulation set object
		@id ws KBasePhenotypes.PhenotypeSimulationSet
	*/
    typedef string phenotypesimulationset_ref;
    /*
		Reference to metabolic model
		@id ws KBaseFBA.FBAModel
	*/
    typedef string fbamodel_ref;
	/*
		KBase genome ID
		@id kb
	*/
    typedef string genome_id;
    /*
		KBase FBA ID
		@id kb
	*/
    typedef string fba_id;
    /*
		Biomass reaction ID
		@id external
	*/
    typedef string biomass_id;
    /*
		Gapgeneration solution ID
		@id external
	*/
    typedef string gapgensol_id;
    /*
		Model compartment ID
		@id external
	*/
    typedef string modelcompartment_id;
    /*
		Model compound ID
		@id external
	*/
    typedef string modelcompound_id;
    /*
		Model reaction ID
		@id external
	*/
    typedef string modelreaction_id;
    /*
		Source ID
		@id external
	*/
    typedef string source_id;
    /*
		Gapgen ID
		@id kb
	*/
    typedef string gapgen_id;
	/*
		Gapfill ID
		@id kb
	*/
    typedef string gapfill_id;
    /*
		Gapfill solution ID
		@id external
	*/
    typedef string gapfillsol_id;
    /*
		FBAModel ID
		@id kb
	*/
    typedef string fbamodel_id;
	
    /* 
    	BiomassCompound object
    	
		@searchable ws_subset modelcompound_ref coefficient
    */
    typedef structure {
		modelcompound_ref modelcompound_ref;
		float coefficient;
    } BiomassCompound;
    
    /* 
    	Biomass object
    	
		@searchable ws_subset id name other dna rna protein cellwall lipid cofactor energy
		@searchable ws_subset biomasscompounds.[*].(modelcompound_ref,coefficient)
    */
    typedef structure {
		biomass_id id;
		string name;
		float other;
		float dna;
		float rna;
		float protein;
		float cellwall;
		float lipid;
		float cofactor;
		float energy;
		list<BiomassCompound> biomasscompounds;
    } Biomass;

    /* 
    	ModelCompartment object
    	
		@searchable ws_subset id compartment_ref compartmentIndex label pH potential
    */
    typedef structure {
		modelcompartment_id id;
		compartment_ref compartment_ref;
		int compartmentIndex;
		string label;
		float pH;
		float potential;
    } ModelCompartment;
    
    /* 
    	ModelCompound object
    	
		@searchable ws_subset id compound_ref name charge formula modelcompartment_ref
    */
    typedef structure {
		modelcompound_id id;
		compound_ref compound_ref;
		string name;
		float charge;
		string formula;
		modelcompartment_ref modelcompartment_ref;
    } ModelCompound;
    
    /* 
    	ModelReactionReagent object
    	
		@searchable ws_subset modelcompound_ref coefficient
    */
    typedef structure {
		modelcompound_ref modelcompound_ref;
		float coefficient;
    } ModelReactionReagent;
    
    /* 
    	ModelReactionProteinSubunit object
    	
		@searchable ws_subset role triggering optionalSubunit feature_refs
    */
    typedef structure {
		string role;
		bool triggering;
		bool optionalSubunit;
		string note;
		list<feature_ref> feature_refs;
    } ModelReactionProteinSubunit;
    
    /* 
    	ModelReactionProtein object
    	 
		@searchable ws_subset complex_ref modelReactionProteinSubunits.[*].(role,triggering,optionalSubunit,feature_refs)
    */
    typedef structure {
		complex_ref complex_ref;
		string note;
		list<ModelReactionProteinSubunit> modelReactionProteinSubunits;
    } ModelReactionProtein;
    
    /* 
    	ModelReaction object
    	
		@searchable ws_subset id reaction_ref direction protons modelcompartment_ref probability
		@searchable ws_subset modelReactionReagents.[*].(modelcompound_ref,coefficient)
		@searchable ws_subset modelReactionProteins.[*].(complex_ref,modelReactionProteinSubunits.[*].(role,triggering,optionalSubunit,feature_refs))
    */
    typedef structure {
		modelreaction_id id;
		reaction_ref reaction_ref;
		string direction;
		float protons;
		modelcompartment_ref modelcompartment_ref;
		float probability;
		list<ModelReactionReagent> modelReactionReagents;
		list<ModelReactionProtein> modelReactionProteins;
    } ModelReaction;

    /* 
    	ModelGapfill object
    	 
		@searchable ws_subset gapfill_id gapfill_ref integrated media_ref ko_refs
    */
    typedef structure {
		gapfill_id gapfill_id;
		gapfill_ref gapfill_ref;
		bool integrated;
		int integrated_solution;
		media_ref media_ref;
    } ModelGapfill;
    
    /* 
    	ModelGapgen object
    	
		@searchable ws_subset gapgen_id gapgen_ref integrated media_ref ko_refs
    */
    typedef structure {
    	gapgen_id gapgen_id;
		gapgen_ref gapgen_ref;
		bool integrated;
		int integrated_solution;
		media_ref media_ref;
    } ModelGapgen;
    
    /* 
    	FBAModel object
    	
    	@optional metagenome_otu_ref metagenome_ref genome_ref
    	@searchable ws_subset id source_id source name type genome_ref metagenome_ref metagenome_otu_ref template_ref
    	@searchable ws_subset gapfillings.[*].(gapfill_id,gapfill_ref,integrated,media_ref,integrated_solution,ko_refs) 
    	@searchable ws_subset gapgens.[*].(gapgen_id,gapgen_ref,integrated,media_ref,integrated_solution,ko_refs) 
    	@searchable ws_subset biomasses.[*].(id,name,other,dna,rna,protein,cellwall,lipid,cofactor,energy,biomasscompounds.[*].(modelcompound_ref,coefficient)) 
    	@searchable ws_subset modelcompartments.[*].(id,compartment_ref,compartmentIndex,label,pH,potential) 
    	@searchable ws_subset modelcompounds.[*].(id,compound_ref,name,charge,formula,modelcompartment_ref)
    	@searchable ws_subset modelreactions.[*].(id,reaction_ref,direction,protons,modelcompartment_ref,probability,modelReactionReagents.[*].(modelcompound_ref,coefficient),modelReactionProteins.[*].(complex_ref,modelReactionProteinSubunits.[*].(role,triggering,optionalSubunit,feature_refs))) 
    */
    typedef structure {
		fbamodel_id id;
		string source;
		source_id source_id;
		string name;
		string type;
		genome_ref genome_ref;
		metagenome_ref metagenome_ref;
		metagenome_otu_ref metagenome_otu_ref;
		template_ref template_ref;
		
		list<ModelGapfill> gapfillings;
		list<ModelGapgen> gapgens;
		
		list<Biomass> biomasses;
		list<ModelCompartment> modelcompartments;
		list<ModelCompound> modelcompounds;
		list<ModelReaction> modelreactions;
    } FBAModel;
    
    /* 
    	FBAConstraint object
    	
    	@searchable ws_subset name rhs sign compound_terms reaction_terms
    */
    typedef structure {
    	string name;
    	float rhs;
    	string sign;
    	mapping<modelcompound_ref,float> compound_terms;
    	mapping<modelreaction_ref,float> reaction_terms;
	} FBAConstraint;
    
    /* 
    	FBAReactionBound object
    	
    	@searchable ws_subset modelreaction_ref variableType upperBound lowerBound
    */
    typedef structure {
    	modelreaction_ref modelreaction_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
	} FBAReactionBound;
    
    /* 
    	FBACompoundBound object
    	
    	@searchable ws_subset modelcompound_ref variableType upperBound lowerBound
    */
     typedef structure {
    	modelcompound_ref modelcompound_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
	} FBACompoundBound;
    
    /* 
    	FBACompoundVariable object
    	
    	@searchable ws_subset modelcompound_ref variableType upperBound lowerBound class min max value
    */
    typedef structure {
    	modelcompound_ref modelcompound_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
    	string class;
    	float min;
    	float max;
    	float value;
	} FBACompoundVariable;
	
	/* 
    	FBAReactionVariable object
    	
    	@searchable ws_subset modelreaction_ref variableType upperBound lowerBound class min max value
    */
	typedef structure {
    	modelreaction_ref modelreaction_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
    	string class;
    	float min;
    	float max;
    	float value;
	} FBAReactionVariable;
	
	/* 
    	FBABiomassVariable object
    	
    	@searchable ws_subset biomass_ref variableType upperBound lowerBound class min max value
    */
	typedef structure {
    	biomass_ref biomass_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
    	string class;
    	float min;
    	float max;
    	float value;
	} FBABiomassVariable;
	
	/* 
    	FBAPromResult object
    	
    	@searchable ws_subset objectFraction alpha beta
    */
	typedef structure {
    	float objectFraction;
    	float alpha;
    	float beta;
	} FBAPromResult;
    
    /* 
    	FBADeletionResult object
    	
    	@searchable ws_subset feature_refs growthFraction
    */
    typedef structure {
    	list<feature_ref> feature_refs;
    	float growthFraction;
	} FBADeletionResult;
	
	/* 
    	FBAMinimalMediaResult object
    	
    	@searchable ws_subset essentialNutrient_refs optionalNutrient_refs
    */
	typedef structure {
    	list<compound_ref> essentialNutrient_refs;
    	list<compound_ref> optionalNutrient_refs;
	} FBAMinimalMediaResult;
    
    /* 
    	FBAMetaboliteProductionResult object
    	
    	@searchable ws_subset modelcompound_ref maximumProduction
    */
    typedef structure {
    	modelcompound_ref modelcompound_ref;
    	float maximumProduction;
	} FBAMetaboliteProductionResult;
    
    /* 
    	FBA object holds the formulation and results of a flux balance analysis study
    	
    	@searchable ws_subset comboDeletions id fva fluxMinimization findMinimalMedia allReversible simpleThermoConstraints thermodynamicConstraints noErrorThermodynamicConstraints minimizeErrorThermodynamicConstraints
    	@searchable ws_subset regmodel_ref fbamodel_ref prommodel_ref media_ref phenotypeset_ref geneKO_refs reactionKO_refs additionalCpd_refs objectiveValue phenotypesimulationset_ref
    	@searchable ws_subset FBAConstraints.[*].(name,rhs,sign,compound_terms,reaction_terms) 
    	@searchable ws_subset FBAReactionBounds.[*].(modelreaction_ref,variableType,upperBound,lowerBound)
    	@searchable ws_subset FBACompoundBounds.[*].(modelcompound_ref,variableType,upperBound,lowerBound)
    	@searchable ws_subset FBACompoundVariables.[*].(modelcompound_ref,variableType,upperBound,lowerBound,class,min,max,value)
		@searchable ws_subset FBAReactionVariables.[*].(modelreaction_ref,variableType,upperBound,lowerBound,class,min,max,value)
		@searchable ws_subset FBABiomassVariables.[*].(biomass_ref,variableType,upperBound,lowerBound,class,min,max,value)
		@searchable ws_subset FBAPromResults.[*].(objectFraction,alpha,beta)
		@searchable ws_subset FBADeletionResults.[*].(feature_refs,growthFraction)
		@searchable ws_subset FBAMinimalMediaResults.[*].(essentialNutrient_refs,optionalNutrient_refs)
		@searchable ws_subset FBAMetaboliteProductionResults.[*].(modelcompound_ref,maximumProduction)
    */
    typedef structure {
		fba_id id;
		bool fva;
		bool fluxMinimization;
		bool findMinimalMedia;
		bool allReversible;
		bool simpleThermoConstraints;
		bool thermodynamicConstraints;
		bool noErrorThermodynamicConstraints;
		bool minimizeErrorThermodynamicConstraints;
		
		bool maximizeObjective;
		mapping<modelcompound_ref,float> compoundflux_objterms;
    	mapping<modelreaction_ref,float> reactionflux_objterms;
		mapping<biomass_ref,float> biomassflux_objterms;
		
		int comboDeletions;
		int numberOfSolutions;
		
		float objectiveConstraintFraction;
		float defaultMaxFlux;
		float defaultMaxDrainFlux;
		float defaultMinDrainFlux;
		float PROMKappa;
		
		bool decomposeReversibleFlux;
		bool decomposeReversibleDrainFlux;
		bool fluxUseVariables;
		bool drainfluxUseVariables;
		
		regmodel_ref regmodel_ref;
		fbamodel_ref fbamodel_ref;
		prommodel_ref prommodel_ref;
		media_ref media_ref;
		phenotypeset_ref phenotypeset_ref;
		list<feature_ref> geneKO_refs;
		list<modelreaction_ref> reactionKO_refs;
		list<compound_ref> additionalCpd_refs;
		mapping<string,float> uptakeLimits;
		
		mapping<string,string> parameters;
		mapping<string,string> inputfiles;
		
		list<FBAConstraint> FBAConstraints;
		list<FBAReactionBound> FBAReactionBounds;
		list<FBACompoundBound> FBACompoundBounds;
			
		float objectiveValue;
		mapping<string,string> outputfiles;
		phenotypesimulationset_ref phenotypesimulationset_ref;

		list<FBACompoundVariable> FBACompoundVariables;
		list<FBAReactionVariable> FBAReactionVariables;
		list<FBABiomassVariable> FBABiomassVariables;
		list<FBAPromResult> FBAPromResults;
		list<FBADeletionResult> FBADeletionResults;
		list<FBAMinimalMediaResult> FBAMinimalMediaResults;
		list<FBAMetaboliteProductionResult> FBAMetaboliteProductionResults;
    } FBA;
    
    /* 
    	GapGenerationSolutionReaction object holds data a reaction proposed to be removed from the model
    	
    	@searchable ws_subset modelreaction_ref direction
    */
    typedef structure {
    	modelreaction_ref modelreaction_ref;
    	string direction;
    } GapgenerationSolutionReaction;
    
    /* 
    	GapGenerationSolution object holds data on a solution proposed by the gapgeneration command
    	
    	@searchable ws_subset id suboptimal gapgenSolutionReactions.[*].(modelreaction_ref,direction) integrated biomassSuppplement_refs mediaRemoval_refs additionalKO_refs 
    */
    typedef structure {
    	gapgensol_id id;
    	float solutionCost;
    	list<modelcompound_ref> biomassSuppplement_refs;
    	list<modelcompound_ref> mediaRemoval_refs;
    	list<modelreaction_ref> additionalKO_refs;
    	bool integrated;
    	bool suboptimal;
    	list<GapgenerationSolutionReaction> gapgenSolutionReactions;
    } GapgenerationSolution;
    
    /* 
    	GapGeneration object holds data on formulation and solutions from gapgen analysis
    	
    	@searchable ws_subset id totalTimeLimit timePerSolution referenceMedia_ref fbamodel_ref fba_ref reactionRemovalHypothesis gprHypothesis biomassHypothesis mediaHypothesis
    	@searchable ws_subset gapgenSolutions.[*].(id,suboptimal,gapgenSolutionReactions.[*].(modelreaction_ref,direction),integrated,biomassSuppplement_refs,mediaRemoval_refs,additionalKO_refs)    	
    */
    typedef structure {
    	gapgen_id id;
    	fba_ref fba_ref;
    	fbamodel_ref fbamodel_ref;
    	
    	bool mediaHypothesis;
    	bool biomassHypothesis;
    	bool gprHypothesis;
    	bool reactionRemovalHypothesis;
    	
    	media_ref media_ref;
    	media_ref referenceMedia_ref;
    	
    	int timePerSolution;
    	int totalTimeLimit;
    	
    	list<GapgenerationSolution> gapgenSolutions;
    } Gapgeneration;
    
    /* 
    	GapFillingReaction object holds data on a reaction added by gapfilling analysis
    	
    	@searchable ws_subset reaction_ref compartment_ref direction candidateFeature_refs
    */
    typedef structure {
    	reaction_ref reaction_ref;
    	compartment_ref compartment_ref;
    	string direction;
    	list<feature_ref> candidateFeature_refs;
    } GapfillingReaction;
    
    /* 
    	GapFillingSolution object holds data on a solution generated by gapfilling analysis
    	
    	@searchable ws_subset id suboptimal integrated solutionCost koRestore_refs biomassRemoval_refs mediaSupplement_refs
    	@searchable ws_subset gapfillingSolutionReactions.[*].(reaction_ref,compartment_ref,direction,candidateFeature_refs)
    */
    typedef structure {
    	gapfillsol_id id;
    	float solutionCost;
    	
    	list<modelcompound_ref> biomassRemoval_refs;
    	list<modelcompound_ref> mediaSupplement_refs;
    	list<modelreaction_ref> koRestore_refs;
    	bool integrated;
    	bool suboptimal;
    	
    	list<GapfillingReaction> gapfillingSolutionReactions;
    } GapfillingSolution;
    
    /* 
    	GapFilling object holds data on the formulations and solutions of a gapfilling analysis
    	
    	@searchable ws_subset id totalTimeLimit timePerSolution transporterMultiplier singleTransporterMultiplier biomassTransporterMultiplier noDeltaGMultiplier noStructureMultiplier deltaGMultiplier directionalityMultiplier drainFluxMultiplier reactionActivationBonus allowableCompartment_refs blacklistedReaction_refs targetedreaction_refs guaranteedReaction_refs completeGapfill balancedReactionsOnly reactionAdditionHypothesis gprHypothesis biomassHypothesis fba_ref fbamodel_ref probanno_ref mediaHypothesis
    	@searchable ws_subset gapfillingSolutions.[*].(id,suboptimal,integrated,solutionCost,koRestore_refs,biomassRemoval_refs,mediaSupplement_refs,gapfillingSolutionReactions.[*].(reaction_ref,compartment_ref,direction,candidateFeature_refs))
    */
    typedef structure {
    	gapfill_id id;
    	fba_ref fba_ref;
    	media_ref media_ref;
    	fbamodel_ref fbamodel_ref;
    	probanno_ref probanno_ref;
    	
    	bool mediaHypothesis;
    	bool biomassHypothesis;
    	bool gprHypothesis;
    	bool reactionAdditionHypothesis;
    	bool balancedReactionsOnly;
    	bool completeGapfill;
    	
    	
    	list<reaction_ref> guaranteedReaction_refs;
    	list<reaction_ref> targetedreaction_refs;
    	list<reaction_ref> blacklistedReaction_refs;
    	list<compartment_ref> allowableCompartment_refs;
    	
    	float reactionActivationBonus;
    	float drainFluxMultiplier;
    	float directionalityMultiplier;
    	float deltaGMultiplier;
    	float noStructureMultiplier;
    	float noDeltaGMultiplier;
    	float biomassTransporterMultiplier;
    	float singleTransporterMultiplier;
    	float transporterMultiplier;
    	
    	int timePerSolution;
    	int totalTimeLimit;
    	
    	mapping<reaction_ref,float> reactionMultipliers;
    	list<GapfillingSolution> gapfillingSolutions;
    } Gapfilling;
	
    /* 
    	TemplateBiomassComponent object holds data on a compound of biomass in template
    	
    	@searchable ws_subset id coefficientType class compound_ref compartment_ref
    */
	typedef structure {
    	templatebiomasscomponent_id id;
    	string class;
    	compound_ref compound_ref;
    	compartment_ref compartment_ref;
    	
    	string coefficientType;
    	float coefficient;
    	
    	list<compound_ref> linked_compound_refs;
    	list<float> link_coefficients;
    } TemplateBiomassComponent;
    
    /* 
    	TemplateBiomass object holds data on biomass in template
    	
    	@searchable ws_subset id name type other dna rna protein lipid cellwall cofactor energy
    	@searchable ws_subset templateBiomassComponents.[*].(id,coefficientType,class,compound_ref,compartment_ref) 
    */
	typedef structure {
    	templatebiomass_id id;
    	string name;
    	string type;
    	float other;
    	float dna;
    	float rna;
    	float protein;
    	float lipid;
    	float cellwall;
    	float cofactor;
    	float energy;
    	list<TemplateBiomassComponent> templateBiomassComponents;
    } TemplateBiomass;
    
    /* 
    	TemplateReaction object holds data on reaction in template
    	
    	@searchable ws_subset id direction type reaction_ref compartment_ref complex_refs
    */
	typedef structure {
    	templatereaction_id id;
    	reaction_ref reaction_ref;
    	compartment_ref compartment_ref;
    	list<complex_ref> complex_refs;
    	string direction;
    	string type;
    } TemplateReaction;
    
    /* 
    	ModelTemplate object holds data on how a model is constructed from an annotation
    	    	
    	@optional name
    	@searchable ws_subset id name modelType domain mapping_ref
    	@searchable ws_subset templateReactions.[*].(id,reaction_ref,compartment_ref,complex_refs,direction,type) 
    	@searchable ws_subset templateBiomasses.[*].(id,name,type,other,dna,rna,protein,lipid,cellwall,cofactor,energy,templateBiomassComponents.[*].(id,coefficientType,class,compound_ref,compartment_ref)) 
    */
	typedef structure {
    	modeltemplate_id id;
    	string name;
    	string modelType;
    	string domain;
    	mapping_ref mapping_ref;
    	
    	list<TemplateReaction> templateReactions;
    	list<TemplateBiomass> templateBiomasses;
    } ModelTemplate;
};