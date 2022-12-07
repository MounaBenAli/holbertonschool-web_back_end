export default function createPushNotificationsJobs(jobs, queue) {
  if (!(Array.isArray(jobs))) throw (new Error('Jobs is not an array'));

  jobs.forEach((element) => {
    const job = queue.create('push_notification_code_3', element).save((error) => {
      if (!error) console.log(`Notification job created: ${job.id}`);
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });

      job.on('fail', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      });

      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    });
  });
}
