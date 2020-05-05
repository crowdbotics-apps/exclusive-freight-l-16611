import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import ArticleList38578Navigator from '../features/ArticleList38578/navigator';
import ArticleList38577Navigator from '../features/ArticleList38577/navigator';
import ArticleList38576Navigator from '../features/ArticleList38576/navigator';
import UserProfile38426Navigator from '../features/UserProfile38426/navigator';
import Tutorial38425Navigator from '../features/Tutorial38425/navigator';
import NotificationList38397Navigator from '../features/NotificationList38397/navigator';
import Settings38396Navigator from '../features/Settings38396/navigator';
import Settings38388Navigator from '../features/Settings38388/navigator';
import UserProfile38386Navigator from '../features/UserProfile38386/navigator';
import UserProfile38355Navigator from '../features/UserProfile38355/navigator';
import Tutorial38354Navigator from '../features/Tutorial38354/navigator';
import NotificationList38326Navigator from '../features/NotificationList38326/navigator';
import Settings38325Navigator from '../features/Settings38325/navigator';
import Settings38317Navigator from '../features/Settings38317/navigator';
import UserProfile38315Navigator from '../features/UserProfile38315/navigator';
import ArticleList38277Navigator from '../features/ArticleList38277/navigator';
import ArticleList38276Navigator from '../features/ArticleList38276/navigator';
import ArticleList38275Navigator from '../features/ArticleList38275/navigator';
import UserProfile38265Navigator from '../features/UserProfile38265/navigator';
import Tutorial38264Navigator from '../features/Tutorial38264/navigator';
import NotificationList38236Navigator from '../features/NotificationList38236/navigator';
import Settings38235Navigator from '../features/Settings38235/navigator';
import Settings38227Navigator from '../features/Settings38227/navigator';
import UserProfile38225Navigator from '../features/UserProfile38225/navigator';
import ArticleList38187Navigator from '../features/ArticleList38187/navigator';
import ArticleList38186Navigator from '../features/ArticleList38186/navigator';
import ArticleList38185Navigator from '../features/ArticleList38185/navigator';
import ArticleList38168Navigator from '../features/ArticleList38168/navigator';
import ArticleList38167Navigator from '../features/ArticleList38167/navigator';
import ArticleList38166Navigator from '../features/ArticleList38166/navigator';
import ArticleList38134Navigator from '../features/ArticleList38134/navigator';
import ArticleList38133Navigator from '../features/ArticleList38133/navigator';
import ArticleList38132Navigator from '../features/ArticleList38132/navigator';
import MessengerNavigator from '../features/Messenger/navigator';
import TutorialNavigator from '../features/Tutorial/navigator';
import MapsNavigator from '../features/Maps/navigator';
import CalendarNavigator from '../features/Calendar/navigator';
import CameraNavigator from '../features/Camera/navigator';
import EmailAuthNavigator from '../features/EmailAuth/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {
    SplashScreen: {
      screen: SplashScreen
    },
    //@BlueprintNavigationInsertion
ArticleList38578: { screen: ArticleList38578Navigator },
ArticleList38577: { screen: ArticleList38577Navigator },
ArticleList38576: { screen: ArticleList38576Navigator },
UserProfile38426: { screen: UserProfile38426Navigator },
Tutorial38425: { screen: Tutorial38425Navigator },
NotificationList38397: { screen: NotificationList38397Navigator },
Settings38396: { screen: Settings38396Navigator },
Settings38388: { screen: Settings38388Navigator },
UserProfile38386: { screen: UserProfile38386Navigator },
UserProfile38355: { screen: UserProfile38355Navigator },
Tutorial38354: { screen: Tutorial38354Navigator },
NotificationList38326: { screen: NotificationList38326Navigator },
Settings38325: { screen: Settings38325Navigator },
Settings38317: { screen: Settings38317Navigator },
UserProfile38315: { screen: UserProfile38315Navigator },
ArticleList38277: { screen: ArticleList38277Navigator },
ArticleList38276: { screen: ArticleList38276Navigator },
ArticleList38275: { screen: ArticleList38275Navigator },
UserProfile38265: { screen: UserProfile38265Navigator },
Tutorial38264: { screen: Tutorial38264Navigator },
NotificationList38236: { screen: NotificationList38236Navigator },
Settings38235: { screen: Settings38235Navigator },
Settings38227: { screen: Settings38227Navigator },
UserProfile38225: { screen: UserProfile38225Navigator },
ArticleList38187: { screen: ArticleList38187Navigator },
ArticleList38186: { screen: ArticleList38186Navigator },
ArticleList38185: { screen: ArticleList38185Navigator },
ArticleList38168: { screen: ArticleList38168Navigator },
ArticleList38167: { screen: ArticleList38167Navigator },
ArticleList38166: { screen: ArticleList38166Navigator },
ArticleList38134: { screen: ArticleList38134Navigator },
ArticleList38133: { screen: ArticleList38133Navigator },
ArticleList38132: { screen: ArticleList38132Navigator },
Messenger: { screen: MessengerNavigator },
Tutorial: { screen: TutorialNavigator },
Maps: { screen: MapsNavigator },
Calendar: { screen: CalendarNavigator },
Camera: { screen: CameraNavigator },
EmailAuth: { screen: EmailAuthNavigator },

    /** new navigators can be added here */
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu,
    initialRouteName: 'SplashScreen',
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
