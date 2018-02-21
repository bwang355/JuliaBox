println("Printing Flow Matrices")
open("./Flow_Output/flow_p1_results_"*"$(epsilon)"*".csv", "w") do f1
open("./Flow_Output/flow_p2_results_"*"$(epsilon)"*".csv", "w") do f2
open("./Flow_Output/flow_p3_results_"*"$(epsilon)"*".csv", "w") do f3
open("./Flow_Output/flow_p4_results_"*"$(epsilon)"*".csv", "w") do f4
open("./Flow_Output/flow_p5_results_"*"$(epsilon)"*".csv", "w") do f5
#open("flow_p4_results.csv", "w") do f4
#open("flow_p5_results.csv", "w") do f5

	for f in [f1,f2,f3,f4,f5]

		if f == f1
			p = "p1"
		elseif f == f2
			p = "p2"
		elseif f == f3
			p = "p3"
		elseif f == f4
			p = "p4"
		elseif f == f5
			p = "p5"
		end
		#show(p)
		print(f,",")

		for j in NODES			# Prints the header with node index
			print(f,j,",")
		end
		println(f,"")			# Used to enter next line

		for j in NODES			# Prints the 1st row entry i.e. the sender node
			print(f,j,",")
		for k in NODES			# Prints the flow value from node j to node k with product p
		       print(f,getvalue(flow[j,k,p]),",")
	        end

	        println(f)
	        end
	end

end
end
end
end
end
