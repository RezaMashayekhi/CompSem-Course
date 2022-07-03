package multi;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

import com.babelscape.util.UniversalPOS;

import edu.mit.jwi.item.ISynset;
import edu.mit.jwi.item.IWord;
import edu.mit.jwi.item.POS;
import it.uniroma1.lcl.babelnet.*;
import it.uniroma1.lcl.babelnet.data.BabelLemma;
import it.uniroma1.lcl.babelnet.data.BabelSenseSource;
import it.uniroma1.lcl.jlt.jgrapht.WordNetGraph;
import it.uniroma1.lcl.jlt.util.*;
import it.uniroma1.lcl.jlt.wordnet.WordNetVersion;
import it.uniroma1.lcl.jlt.wordnet.*;
import it.uniroma1.lcl.kb.ResourceID;


public class C {
	 public static void main(String[] args) throws IOException {
	        System.out.println("Hello, World!"); 
	        BabelNet bn = BabelNet.getInstance();
	        WordNet wn = WordNet.getInstance(WordNetVersion.WN_30);
	        
	        FileWriter myWriter = new FileWriter("babelnet.txt");
			
	        Set<ISynset> wnl = wn.getAllSynsets();
	        
	        for (Iterator iterator = wnl.iterator(); iterator.hasNext();) {
				ISynset iSynset = (ISynset) iterator.next();
				
				String s = iSynset.getWords().get(0).toString().split("-")[1] + iSynset.getWords().get(0).toString().split("-")[2];
				String off = "wn:" + s.toLowerCase();
				s += "\t";
				
				for(Iterator iterator2 = iSynset.getWords().iterator(); iterator2.hasNext();) {
					IWord word = (IWord) iterator2.next();
					s += word.getSenseKey() + ",";
				}
				s += "\t";
				System.out.println(off);
				System.out.println(bn.getSynset(new WordNetSynsetID(off)));
				List<BabelLemma> lemmas = bn.getSynset(new WordNetSynsetID(off)).getLemmas(Language.FA);
				for (Iterator iterator2 = lemmas.iterator(); iterator2.hasNext();) {
					BabelLemma lemma = (BabelLemma) iterator2.next();
					s += lemma + ",";
				}
				myWriter.write(s + "\n"); 
				System.out.println(s);
			}
    	 
  	        myWriter.close();
        
	       
	 }
}
