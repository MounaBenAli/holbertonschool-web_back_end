const kue = require('kue');

const queue = kue.createQueue();

const object = {
  phoneNumber: '',
  message: '',
};

const job = queue.create('push_notification_code', object).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('fail', () => {
  console.log('Notification job failed');
});
