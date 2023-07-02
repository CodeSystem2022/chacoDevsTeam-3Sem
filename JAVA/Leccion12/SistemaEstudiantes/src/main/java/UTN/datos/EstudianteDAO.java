package UTN.datos;

import static UTN.conexion.Conexion.getConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import UTN.dominio.Estudiante;

public class EstudianteDAO {
    //Metod listar
    public List<EstudianteDAO> listarEstudiantes(){
        List<Estudiante> estudiantes = new ArrayList<>();
        //Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; //Envia la sentencia a la base de datos
        ResultSet rs; //Obtenemos el resultado de la base de datos
        //Creamos un objeto de tipo conexion
        Connection con = getConnection();
        String sql = "SELECT * FROM"
    }
}
    //Metodo por id -> fin by id
    public boolean buscarEstudiantePorId(Estudiante estudiante){
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiante2022 WHERE idestudiantes22=?";
        try{
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getEstudiante());
            rs = ps.executeQuery();
            if(rs.next()){
                estudiante.SetNombre(rs.getString("nombre"));
                estudiante.SetApellido(rs.getString("apellido"));
                estudiante.SetTelefono(rs.getString("telefono"));
                estudiante.SetEmail(rs.getString("email"));
                return true; //Se encontro un registro
            }//Fin if
        }catch (Exception e){
            System.out.println("Ocurrio un error al buscar estudiante: "+e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("Ocurrio un error al cerrar la conexión: "+e.getMessage());
            }//fin catch
        }//fin finally
        return false;
    }

    //Metodo agregar un nuevo estudiante
    public boolean agregarEstudiante(Estudiante estudiante){
    PreparedStatement ps;
    Connection con = getConnection();
    String sql = 'INSERT INTO estudiantes2022(nombre, apellido, telefono, email) VALUES (?,?,?,?)';
    TRY{
        ps = con.prepareStatement(sql);
        ps.setString(1, estudiante.getNombre());
        ps.setString(2, estudiante.getApellido());
        ps.setString(3, estudiante.getTelefono());
        ps.setString(4, estudiante.getEmail());
        ps.execute();
        return true;
        }catch(Exception e){
            System.out.println("Ocurrio un Error al agregar estudiante"+e.getMessage());
        }//Fin catch
        finally{
        try{
            con.close();
        }catch (Exception e){
            System.out.println("Error al cerrar la conexion: "+e.getMessage());
        }//fin catch
        }//fin finally
        return false;
    }//Fin metodo agregarEstudiante

    public static void main(String[] args) {
        //Listar los estudiantes
        var estudianteDao = new EstudianteDAO();
        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudianteDao.listarestudiantes();
        estudiantes.forEach(System.out::println); // Funcion lamda para imporimir
    }