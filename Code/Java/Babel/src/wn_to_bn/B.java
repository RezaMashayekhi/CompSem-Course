package wn_to_bn;

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


public class B {
	 public static void main(String[] args) throws IOException {
	        System.out.println("Hello, World!"); 
	        BabelNet bn = BabelNet.getInstance();
	        
	        
	        FileWriter myWriter = new FileWriter("bn_senses.txt");
	        File myObj = new File("wn_senses.txt");
	        Scanner myReader = new Scanner(myObj);
	        
	        while (myReader.hasNextLine()) {
	        	String data = myReader.nextLine();
	        	System.out.println(data);
	        	String id = "";
	        	if (data.split(" ").length>2) {
	        		id = data.split(" ")[2];
	        	}
	        	else {
	        		id = data.split(" ")[1];
	        	}
	        	//System.out.println(data.split(" ")[1]);
	        	//System.out.println(data.split(" ")[2]);
	        	//System.out.println( bn.getSynset(new WordNetSynsetID("wn:05122099n")).getId());
	        	if(! id.equals("U")) {
	        		try{
	        			myWriter.write(data.split(" ")[0] + " " + bn.getSynset(new WordNetSynsetID(id)).getId() + "\n");
	        		}
	        		catch(Exception e){
	        			myWriter.write(data.split(" ")[0] + " " + "U" + "\n");
	        		}
	        		finally {
	        			
	        		}
	        	}
	        	else {
	        		myWriter.write(data.split(" ")[1] + " " + "U" + "\n");
	        	}
	        	  
	        } 
	        myWriter.close();
	        
	        //System.out.println(byl);
	        //BabelSynset by = bn.getSynset(new BabelSynsetID("bn:03083790n"));
	 }
}
