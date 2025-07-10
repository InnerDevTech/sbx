using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{
    private float _speed1 = 3.0f;

    // Start is called before the first frame update
    void Start()
    {

    }

    void Update()
    {
        transform.Translate(Vector3.down * _speed1 * Time.deltaTime);

        if (transform.position.y < -8f)
        {
            transform.position = new Vector3(Random.Range(-10.0f, 10.0f), 8, 0);
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Player")
        {
            Player player = other.GetComponent<Player>();
            if (player != null)
            {
                player.Damage();
            }
        }

        if (other.tag == "Laser")
        {
            Destroy(this.gameObject);
            Destroy(other.gameObject);
            Debug.Log(other.tag);
        }
    }
}
