// C++ structure de données


// 1 : array (tableau statique)
#include <array>
std::array<int, 5> a = {1, 2, 3, 4, 5};
int n = a.size();
int e = a.at(0); // accès à l'élément à l'index 0 avec vérification
int e2 = a[0]; // accès à l'élément à l'index 0

// 2 : vector (liste dynamique)
#include <vector>
std::vector<int> v = {1, 2, 3};
v.push_back(4);
int e = v.pop_back();
int n = v.size();
v.insert(0, 5); // insérer 5 à la position 0
v.erase(0); // supprimer l'élément à la position 0

// 3 : list (liste chaînée)
#include <list>
std::list<int> l = {1, 2, 3};
l.push_back(4);
l.push_front(0);
int e = l.pop_back();
int e2 = l.pop_front();
l.insert(l.begin(), 5); // insérer 5 au début

// 4 : map ou unordered_map (dictionnaire)
#include <map>
#include <unordered_map> // dico

std::map<std::string, int> m = {{"a", 1}, {"b", 2}};
std::unordered_map<std::string, int> um = {{"a", 1}, {"b", 2}};
m["a"] = 3; 
int e = m["a"];
int e2 = m.at("a"); 
m.insert({"c", 3}); 
m.erase("a");

// 5 : set ou unordered_set (table de hachage)
#include <set>
std::set<int> s = {1, 2, 3};
s.insert(4);
s.erase(2); // supprimer 2
int e = s.find(3); // trouver 3

// 6 : pair (deux valeurs)
#include <pair>
std::pair<int, int> p = {1, 2};

// 7 : string (chaîne de caractères)
#include <string>
std::string s = "Hello";
int n = s.length();
int ss = s.substr(0, 2); // sous-chaîne de 0 à 2 inclu
int e = s.find("l"); // position de la première occurrence de 'l'
int e2 = s.find("l", 2); // position de la première occurrence de 'l' après l'index 2

// 8 : queue ou deque (file d'attente)

// 9 : fstream (flux de fichiers)
#include <fstream>
std::ifstream file("file.txt"); // ouvrir un fichier en lecture
std::ofstream file("file.txt"); // ouvrir un fichier en écriture
std::fstream file("file.txt"); // ouvrir un fichier en lecture et écriture

// 10 : tuple (plusieurs valeurs)

// Librairies
// 1 : iostream (entrées/sorties)
#include <iostream>
int main(){
    int age;
    std::cout << "Quel est votre age ? ";
    std::cin >> age;
    std::cout << "Vous avez " << age << " ans." << std::endl;
    return 0;
}

// 2 : cmath (mathématiques)
#include <cmath>
int f(){
    double x = 2.0;
    std::cout << "sqrt " << x << sqrt(x) << std::endl;
}

// 3 : algorithm (algorithmes)
#include <algorithm>
std::vector<int> v = {10, 232, 3};
std::sort(v.begin(), v.end()); // trier le vecteur
std::reverse(v.begin(), v.end()); // inverser le vecteur
std::min(v.at(0), v.at(1)); // minimum entre deux éléments
std::find(v.begin(), v.end(), 3); // trouver un élément

// 5 : cstdlib (fonctions utilitaires)
#include <cstdlib>
rand() // générer un nombre aléatoire
srand(time(0)); // initialiser le générateur de nombres aléatoires
atoi("123"); // convertir une chaîne en entier
exit(0); // quitter le programme