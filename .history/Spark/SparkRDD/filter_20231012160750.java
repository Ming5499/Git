package filter;

import java.util.Arrays;
import java.util.List;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;

public class filter {
	public static void main(String[] args) {
		SparkConf conf = new SparkConf()
				.setAppName("Demo")
				.setMaster("local[2]");
	
		try (JavaSparkContext sc = new JavaSparkContext(conf)) {
			List<Integer> list = Arrays.asList(10,11,12,13,14,15);
			JavaRDD<Integer> data = sc.parallelize(list);
			
			data = data.filter(new Function<Integer, Boolean>() {
				private static final long serialVersionUID = 1L;

				@Override
				public Boolean call(Integer v1) throws Exception {
					if(v1 % 5 == 0) return true;
					return false;
				}
			});
			
			data.collect().forEach(v -> System.out.println(v));
		}
	}
}