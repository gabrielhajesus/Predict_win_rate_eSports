import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:predict/src/feature/home/data/home_repository.dart';

class TeamDetailsPage extends StatefulWidget {
  final Map<String, dynamic> item;
  TeamDetailsPage({required this.item});
  @override
  _TeamDetailsPageState createState() => _TeamDetailsPageState(item: item);
}

class _TeamDetailsPageState extends State<TeamDetailsPage> {
  final Map<String, dynamic> item;
  _TeamDetailsPageState({required this.item});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Detalhes do Time'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            SizedBox(
                height: 100,
                width: 100,
                child: Image.network(item['team_1_img'])),
            Text(item['team_1'],
                style:
                    const TextStyle(fontWeight: FontWeight.bold, fontSize: 12),
                overflow: TextOverflow.ellipsis),
            Column(
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                if (item['desconto'] != 0) ...[
                  Text(
                    "${item['desconto']}%",
                    style: const TextStyle(fontSize: 12),
                    textAlign: TextAlign.end,
                  )
                ],
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(item['old_price'],
                        textAlign: TextAlign.center,
                        style: const TextStyle(fontSize: 16),
                        overflow: TextOverflow.ellipsis),
                    Text(item['menor_preco'],
                        textAlign: TextAlign.center,
                        style: const TextStyle(fontSize: 16),
                        overflow: TextOverflow.ellipsis),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
