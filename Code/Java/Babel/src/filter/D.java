package filter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

import com.babelscape.util.UniversalPOS;

import edu.mit.jwi.item.POS;
import it.uniroma1.lcl.babelnet.*;
import it.uniroma1.lcl.babelnet.data.BabelLemma;
import it.uniroma1.lcl.babelnet.data.BabelSenseSource;
import it.uniroma1.lcl.jlt.jgrapht.WordNetGraph;
import it.uniroma1.lcl.jlt.util.*;
import it.uniroma1.lcl.jlt.wordnet.*;
import it.uniroma1.lcl.kb.ResourceID;


public class D {
	public static void main(String[] args) throws IOException {
        System.out.println("Hello, World!"); 
        BabelNet bn = BabelNet.getInstance();
        WordNet wn = WordNet.getInstance();
	    WordNetFrequencies wnf = WordNetFrequencies.getInstance();
	        
        
        FileWriter myWriter = new FileWriter("fa_blind_test_key_proj_f.txt");
        File myObj = new File("lemma_u_d.txt");
        Scanner myReader = new Scanner(myObj);
        
        while (myReader.hasNextLine()) {
        	String data = myReader.nextLine();
        	System.out.println(data);
        	String id = "";
        	/*
        	if (data.split(" ").length>2) {
        		id = data.split(" ")[2];
        	}
        	else {
        		id = data.split(" ")[1];
        	}
        	*/
        	id = data.split("#")[1];
        	System.out.println(data.split("#")[0]);
        	String olemma = data.split("#")[0];
        	//System.out.println(data.split(" ")[1]);
        	//System.out.println(data.split(" ")[2]);
        	//System.out.println( bn.getSynset(new WordNetSynsetID("wn:05122099n")).getId());
        	if(! id.equals("U")) {
        		try{
        			List<BabelLemma> lemmas = bn.getSynset(new BabelSynsetID(id)).getLemmas(Language.FA);
        			boolean f = false;
    				for (Iterator iterator2 = lemmas.iterator(); iterator2.hasNext();) {
    					BabelLemma lemma = (BabelLemma) iterator2.next();
    					if(lemma.equals(olemma)) {
    						f= true;
    					}
    				}
    				if (f== false) {
    					BabelNetQuery query = new BabelNetQuery.Builder(olemma)
    		  	        	    .from(Language.FA)
    		  	        	    .source(BabelSenseSource.WN)
    		  	        	    .build();
    		  	        
    		  	        List<BabelSynset> byl = bn.getSynsets(query);
    		  	        
    		  	        //part A
	  		  	        if (byl.size()>0) {
	  		  	        	int m = 0;
	  		  	        	int index = 0;
	  		  	        	for (int i = 0; i < byl.size(); i++) {
	  		  	        		if (wnf.getSenseFrequency(byl.get(i).toString()) > m) {
	  		  	        			m = wnf.getSenseFrequency(byl.get(i).toString());
	  		  	        			index = i;
	  		  	        		}
	  		  	        	}
	  		  	        	String sense = "";
	  		  	        	try{
	  		  	        		sense = wn.getSenseFromSenseString(byl.get(index).toString()).toString();
	  		  	        		sense = "wn:" + sense.split("-")[1] + sense.split("-")[2].toLowerCase();
	  			  	        	sense = bn.getSynset(new WordNetSynsetID(sense)).getId().toString();
	  		  	        	}
	  		  	        	catch(Exception e){
	  		  	        		sense = byl.get(index).getId().toString();
	  		  	        	}
	  		  	        	finally {
	  			  	        	
	  			  	        	id = sense;
	  		  	        	}
	  		
	  		  	        }
	  		  	        else {
	  		  	        	query = new BabelNetQuery.Builder(olemma)
	  			  	        	    .from(Language.FA)
	  			  	        	    .build();
	  			  	        
	  			  	        byl = bn.getSynsets(query);
	  			  	        System.out.println(byl);
	  			  	        if (byl.size() > 0) {
	  			  	        	id = byl.get(0).getId().toString();
	  			  	        }
	  			  	        else {
	  			  	        	id = "U";
	  			  	        }
	  		  	        	
	  		  	        }
    		  	        
    				}
    				
    				
    

        			myWriter.write(data.split("#")[0] + " " + id + "\n");
        		}
        		catch(Exception e){
        			myWriter.write(data.split("#")[0] + " " + "U" + "\n");
        		}
        		finally {
        			
        		}
        	}
        	else {
        		myWriter.write(data.split("#")[0] + " " + "U" + "\n");
        	}
        	  
        } 
        myWriter.close();
        
 }
}
