import React from 'react';
import { Card } from '../Components/Ui/export.js';

function PrivacyPolicy() {
  return (
    <div className="text-text-primary mx-auto max-w-5xl px-4 py-10">
      {/* Page Title */}
      <div className="mb-8">
        <h1 className="mb-2 text-3xl font-bold">Privacy Policy</h1>
        <p className="text-text-secondary">
          Your privacy matters to us. This policy explains how PyChat collects, uses, and protects
          your information.
        </p>
      </div>

      <div className="space-y-6">
        <Card title="1. Information We Collect">
          <p>
            We collect only the information necessary to provide and improve PyChat services. This
            may include:
          </p>
          <ul className="text-text-secondary mt-3 list-inside list-disc space-y-1">
            <li>Account details such as name, email, and username</li>
            <li>Messages and metadata required for chat functionality</li>
            <li>Device and usage data for security and performance</li>
          </ul>
        </Card>

        <Card title="2. How We Use Your Information">
          <p className="text-text-secondary">Your information is used strictly to:</p>
          <ul className="text-text-secondary mt-3 list-inside list-disc space-y-1">
            <li>Provide secure, real-time messaging</li>
            <li>Maintain account integrity and prevent misuse</li>
            <li>Improve product features and user experience</li>
          </ul>
        </Card>

        <Card title="3. End-to-End Encryption">
          <p className="text-text-secondary">
            PyChat uses end-to-end encryption to protect your messages. This means only you and the
            intended recipient can read the content of your conversations. PyChat does not access or
            store readable message content.
          </p>
        </Card>

        <Card title="4. Data Sharing">
          <p className="text-text-secondary">
            We do not sell, trade, or rent your personal data. Information is shared only when
            required by law or to protect the safety and security of our users and platform.
          </p>
        </Card>

        <Card title="5. Data Security">
          <p className="text-text-secondary">
            We implement industry-standard security practices including encryption, access controls,
            and continuous monitoring to protect your data from unauthorized access or disclosure.
          </p>
        </Card>

        <Card title="6. Your Rights">
          <p className="text-text-secondary">
            You have the right to access, update, or delete your account information. You may also
            request clarification on how your data is handled by contacting our support team.
          </p>
        </Card>

        <Card title="7. Changes to This Policy">
          <p className="text-text-secondary">
            PyChat may update this Privacy Policy from time to time. Any changes will be reflected
            on this page, and continued use of the platform constitutes acceptance of the updated
            policy.
          </p>
        </Card>

        <Card title="8. Contact Us" footer="Last updated: August 2025">
          <p className="text-text-secondary">
            If you have questions or concerns regarding this Privacy Policy, please contact us at{' '}
            <span className="text-accent font-medium">support@pychat.app</span>.
          </p>
        </Card>
      </div>
    </div>
  );
}

export default PrivacyPolicy;
