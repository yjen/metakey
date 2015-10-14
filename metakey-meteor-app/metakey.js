Status = new Mongo.Collection("status");

if (Meteor.isClient) {
  Template.Home.events({
    "click .square-button": function () {
      var id = Status.find().fetch()[0]._id;
      Status.update(id, {
        $set: { releasing: true, time: new Date() }
      });
      setTimeout(function () {
        Status.update(id, {
          $set: { releasing: false, time: new Date() }
        });
      }, 10000);
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    if (Status.find().count() == 0) {
      Status.insert({ releasing: false, time: new Date()});
    }
  });
}

Router.route('/', {
  template: 'Home'
});

Router.map(function() {
  this.route('api', {
    path: '/api',
    where: 'server',
    action: function() {
      var json = Status.find().fetch();
      this.response.setHeader('Content-Type', 'application/json');
      this.response.end(JSON.stringify(json));
    }
  });
});
