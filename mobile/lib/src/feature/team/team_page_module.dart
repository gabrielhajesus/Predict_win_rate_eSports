import 'package:flutter_modular/flutter_modular.dart';
import 'package:predict/src/feature/team/view/page/teampage.dart';
import '../home/view_model/home_viewmodel.dart';

class TeamPageModule extends Module {
  @override
  final List<Bind> binds = [];

  @override
  final List<ModularRoute> routes = [
    ChildRoute('/',
        child: (_, args) => TeamDetailsPage(
              item: args.data,
            )),
  ];
}
