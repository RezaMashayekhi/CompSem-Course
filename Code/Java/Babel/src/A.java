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
import it.uniroma1.lcl.babelnet.data.BabelSenseSource;
import it.uniroma1.lcl.jlt.jgrapht.WordNetGraph;
import it.uniroma1.lcl.jlt.util.*;
import it.uniroma1.lcl.jlt.wordnet.WordNetVersion;
import it.uniroma1.lcl.jlt.wordnet.*;
import it.uniroma1.lcl.kb.ResourceID;


public class A {
	 public static void main(String[] args) throws IOException {
	        System.out.println("Hello, World!"); 
	        BabelNet bn = BabelNet.getInstance();
	        
	        
	        FileWriter myWriter = new FileWriter("u_to_bn.txt");
	        File myObj = new File("lemma_u.txt");
	        Scanner myReader = new Scanner(myObj);
	        //System.out.println(bn.getSynset(new BabelSynsetID("bn:00009654n")).getWordNetOffsets());
	        while (myReader.hasNextLine()) {
	        	String data = myReader.nextLine();
	        	if (data.split("#").length>1) {
		        	String lemma = data.split("#")[1];
		            //if (lemma.split("_").length>1){
		            //	lemma = lemma.split("_")[0] + " " + lemma.split("_")[1];
		            //	System.out.println(lemma);
		            //}
		        	  
			  	        
		  	        BabelNetQuery query = new BabelNetQuery.Builder(lemma)
		  	        	    .from(Language.ES)
		  	        	    .source(BabelSenseSource.WN)
		  	        	    .build();
		  	        
		  	        List<BabelSynset> byl = bn.getSynsets(query);
		  	        System.out.println(lemma);
		  	        System.out.println(byl);
		  	        
		  	        WordNet wn = WordNet.getInstance();
		  	        WordNetFrequencies wnf = WordNetFrequencies.getInstance();
		  	        
		  	        
		  	        //System.out.println(wn.getSenseFromSenseString("go#v#1"));
		  	        //bn.getSynset(new WordNetSynsetID("01835496"))
		  	        // bn.getSynsets(new WordNetSynsetID("go#v#1"));
		  	       
		  	        //System.out.println(wnf.getLemmaFrequencies("go",POS.VERB).getTop());
		  	        
		  	        //System.out.println(wnf.getSenseFrequency("bad#a#1"));
		  	        //System.out.println(wn.getSenseFromSenseString("bad#a#1"));
		  	        //System.out.println(bn.getSynset(new ResourceID("wn:09359631n", BabelSenseSource.WN));
		  	        //System.out.println(bn.getSynset(new WordNetSynsetID("wn:01835496v")).getId());
		  	        
		  	        /*
		  	        String en_lemmas = data.split("#")[0] + "#" + data.split("#")[1] + "#";
		  	        for (Iterator iterator = byl.iterator(); iterator.hasNext();) {
		  				BabelSynset babelSynset = (BabelSynset) iterator.next();
		  				//wnf.getLemmaFrequencies(lemma, POS.VERB).getTop();
		  				//System.out.println(babelSynset.getWordNetOffsetMapTo(WordNetVersion.WN_21));
		  				//System.out.println(wn.getSenseFromSenseString("bad#a#1"));
		  				en_lemmas += babelSynset.getMainSense().toString().split(":")[2].replace("]", "") + "#" ;
		  	        }
		  	        myWriter.write(en_lemmas + "\n"); 
		  	        */
		  	        String en_lemmas ="";
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
			  	        	
			  	        	en_lemmas = data.split("#")[0] + "#" + data.split("#")[1] + "#" + sense;
		  	        	}
		
		  	        }
		  	        else {
		  	        	//en_lemmas = data.split("#")[0] + "#" + data.split("#")[1] + "#" + "U";
		  	        	
		  	        	query = new BabelNetQuery.Builder(lemma)
			  	        	    .from(Language.ES)
			  	        	    .build();
			  	        
			  	        byl = bn.getSynsets(query);
			  	        System.out.println(byl);
			  	        if (byl.size() > 0) {
			  	        	en_lemmas = data.split("#")[0] + "#" + data.split("#")[1] + "#" + byl.get(0).getId();
			  	        }
			  	        else {
			  	        	en_lemmas = data.split("#")[0] + "#" + data.split("#")[1] + "#" + "U";
			  	        }
		  	        	
		  	        }
		  	        myWriter.write(en_lemmas + "\n"); 
	        	}
	        	  
	        } 
	        myWriter.close();
	        
	        //System.out.println(byl);
	        //BabelSynset by = bn.getSynset(new BabelSynsetID("bn:03083790n"));
	 }
}
