import React from 'react';
import { Card } from '../Components/Ui/export.js';

function Security() {
  return (
    <div className="text-text-primary mx-auto max-w-5xl px-4 py-10">
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="mb-2 text-3xl font-bold">Security at PyChat</h1>
        <p className="text-text-secondary">
          Protecting your data and conversations is our top priority. Learn how PyChat keeps your
          information secure.
        </p>
      </div>

      <div className="space-y-6">
        <Card title="1. End-to-End Encryption">
          <p className="text-text-secondary">
            PyChat uses end-to-end encryption (E2EE) to ensure that only you and your intended
            recipients can read your messages. Message content is encrypted on your device and
            decrypted only on the recipient’s device.
          </p>
        </Card>

        <Card title="2. Secure Authentication">
          <p className="text-text-secondary">
            We protect user accounts with secure authentication mechanisms, including encrypted
            passwords, session protection, and safeguards against unauthorized access.
          </p>
        </Card>

        <Card title="3. Data Protection & Storage">
          <p className="text-text-secondary">
            All sensitive data is encrypted at rest and in transit using industry-standard
            protocols. We follow strict access control policies to limit data exposure to authorized
            systems only.
          </p>
        </Card>

        <Card title="4. Infrastructure Security">
          <p className="text-text-secondary">
            PyChat is hosted on secure cloud infrastructure with firewalls, monitoring, and
            automated threat detection to prevent and respond to potential attacks.
          </p>
        </Card>

        <Card title="5. Regular Security Updates">
          <p className="text-text-secondary">
            We continuously review and update our systems to address emerging threats. Security
            patches and improvements are deployed regularly to maintain platform integrity.
          </p>
        </Card>

        <Card title="6. Abuse & Threat Prevention">
          <p className="text-text-secondary">
            PyChat actively monitors for abusive behavior, spam, and malicious activity. Accounts
            engaging in harmful actions may be restricted or terminated to protect our users.
          </p>
        </Card>

        <Card title="7. Responsible Disclosure">
          <p className="text-text-secondary">
            We welcome responsible disclosure of security vulnerabilities. If you believe you have
            discovered a security issue, please report it to us immediately so we can investigate
            and resolve it promptly.
          </p>
        </Card>

        <Card title="8. Contact Our Security Team" footer="Last updated: August 2025">
          <p className="text-text-secondary">
            For security-related concerns or vulnerability reports, contact us at{' '}
            <span className="text-accent font-medium">security@pychat.app</span>.
          </p>
        </Card>
      </div>
    </div>
  );
}

export default Security;
