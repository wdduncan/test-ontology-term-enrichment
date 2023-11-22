robot reason -i ontology/cancer_instances_50.ttl  \
		--reasoner elk --include-indirect true --axiom-generators "ClassAssertion" \
		-o ontology/cancer_instances_50_reasoned.ttl
