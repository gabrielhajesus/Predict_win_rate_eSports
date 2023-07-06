import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:flutter_svg/svg.dart';
import '../../data/home_repository.dart';
import 'package:http/http.dart' as http;

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Map<String, dynamic>>>(
      future: MongoDataBase().fetchData(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Container(
              alignment: Alignment.center,
              child: const CircularProgressIndicator());
        }

        if (snapshot.hasError) {
          return Container(
              alignment: Alignment.center,
              child: const Text('Erro ao carregar os dados'));
        }

        final data = snapshot.data;

        if (data!.isEmpty) {
          return Container(
            alignment: Alignment.center,
            child: const Text(
              'Nenhum dado encontrado',
              textAlign: TextAlign.center,
            ),
          );
        }

        return Scaffold(
          appBar: AppBar(
            title: const Text('Campeonatos'),
            actions: [
              IconButton(
                icon: Icon(Icons.search),
                onPressed: () {
                  print("pesquisando");
                },
              ),
            ],
          ),
          body: GridView.builder(
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 1,
                crossAxisSpacing: 10.0,
                mainAxisSpacing: 10.0,
              ),
              itemCount: 30,
              itemBuilder: (context, index) {
                final item = data[index];
                return InkWell(
                  onTap: () {
                    Modular.to.pushNamed('/teampage', arguments: item);
                  },
                  child: GridTile(
                    child: Container(
                      decoration: BoxDecoration(
                        border: Border.all(color: Colors.grey),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(item['team_1'],
                              style: const TextStyle(
                                  fontWeight: FontWeight.bold, fontSize: 20),
                              overflow: TextOverflow.ellipsis),
                          SizedBox(
                            height: 50,
                            width: 50,
                            child: item['team_1_img'].toString().contains('png')
                                ? Image.network(
                                    item['team_1_img'],
                                  )
                                : SvgPicture.network(
                                    item['team_1_img'],
                                    fit: BoxFit.fill,
                                  ),
                          ),
                          Text(
                              item['team_1']
                                      .toString()
                                      .contains(item['team_victory'].toString())
                                  ? item['victory_score']
                                  : item['defeat_score'],
                              style: const TextStyle(
                                  fontWeight: FontWeight.bold, fontSize: 20),
                              overflow: TextOverflow.ellipsis),
                          Text(
                              item['team_2']
                                      .toString()
                                      .contains(item['team_victory'].toString())
                                  ? item['victory_score']
                                  : item['defeat_score'],
                              style: const TextStyle(
                                  fontWeight: FontWeight.bold, fontSize: 20),
                              overflow: TextOverflow.ellipsis),
                          SizedBox(
                            height: 50,
                            width: 50,
                            child: item['team_2_img'].toString().contains('png')
                                ? Image.network(item['team_2_img'])
                                : SvgPicture.network(
                                    item['team_2_img'],
                                    fit: BoxFit.fill,
                                  ),
                          ),
                          Text(item['team_2'],
                              style: const TextStyle(
                                  fontWeight: FontWeight.bold, fontSize: 20),
                              overflow: TextOverflow.ellipsis),
                        ],
                      ),
                    ),
                  ),
                );
              }),
        );
      },
    );
  }
}
