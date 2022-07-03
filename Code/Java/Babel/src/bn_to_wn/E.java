package bn_to_wn;

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


public class E {
	public static void main(String[] args) throws IOException {
        System.out.println("Hello, World!"); 
        BabelNet bn = BabelNet.getInstance();
        
        
        FileWriter myWriter = new FileWriter("wordnet.txt");
        File myObj = new File("multinet.txt");
        Scanner myReader = new Scanner(myObj);
        
        while (myReader.hasNextLine()) {
        	String data = myReader.nextLine();
        	System.out.println(data);
        	String sense = data.split("\t")[0];
        	String id ="";
        	try {
        		id = bn.getSynset(new BabelSynsetID(sense)).getWordNetOffsets().get(0).getID();
        	}
        	catch (Exception e) {
				// TODO: handle exception
        		id = "_No_WN_";
			}
        	finally {
        		myWriter.write(id + "\t" + data.split("\t")[1] + "\t" + data.split("\t")[2] + "\n");
			}
        	//System.out.println(sense + "\t" + data.split("\t")[1] + "\t" + data.split("\t")[2]);
        	
        	
        	  
        } 
        myWriter.close();
        
        //System.out.println(byl);
        //BabelSynset by = bn.getSynset(new BabelSynsetID("bn:03083790n"));
 }
}
