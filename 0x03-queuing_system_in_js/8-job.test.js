import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('throws an error if jobs is not an array (Number)', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
  });

  it('throws an error if jobs is not an array (Object)', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
  });

  it('throws an error if jobs is not an array (String)', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
  });

  it('does not throw error if jobs is an empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
  });

  it('does not throw error if jobs is an empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
  });

  it('creates two new jobs in the queue', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    });

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql({
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account',
    });
  });
});
