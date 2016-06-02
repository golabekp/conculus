class dbc{
	
	var $result;
	var $dbuname="experia";
	var $dbpassw="QNV8ySw0qV";
	var $server="as170.experia.com";
	var $database="experia";
	var $db_connection;

	var $numRows;
	var $data;
	
	function __construct()
	{
		
		$db_con=mysqli_connect($this->server, $this->dbuname, $this->dbpassw, $this->database);
		$this->db_connection=$db_con;
		
		if(!$db_con)
		{
			throw new Exception("Please try again connection");
		}	
		//var_dump($db_con);
	}
	
	function result($sql)
	{
		//print($sql);
		$result=mysqli_query($this->db_connection,$sql);

		if(!$result)
		{
			//print($sql);
			throw new Exception("Please try again.");
		}	
		else($result);
		{
			$this->result=$result;
		}
		//var_dump($result);
	}//end of result function

	function ret_result()
	{
		return $this->result;
	}
	
	function NumRows($sql)
	{
		
		$this->result($sql);
		$result=$this->ret_result();
		$numrows=mysqli_num_rows($result);
		$this->numRows=$numrows;
		
	}
	
	function getNumRows()
	{
		
		return $this->numRows;
		
	}
	
	function setData($sql,$fields)
	{
		$this->result($sql);
		$result=$this->ret_result();
		//var_dump($result);
		$this->numRows($sql);
		$numrows=$this->getNumrows();
		
		if($numrows==0)
		{
			
			$this->data['records']=0;
			
		}
		
		else
		{
			
			$this->data['records']=$numrows;
			
			for($i=0;$i<$numrows;$i++)
			{

				if($numrows>0)
				{
					mysqli_data_seek($result,$i);
				}
					
				$db_field=mysqli_fetch_assoc($result);
				foreach($fields as $value)
				{
					$this->data[$value][$i]=$db_field[$value];
				}

			}
			
		}
		
	}
	
	function getData()	
	{
		return $this->data;
	}
	
	function insertData($sql)
	{
		$this->result($sql);	
	}
	
}
