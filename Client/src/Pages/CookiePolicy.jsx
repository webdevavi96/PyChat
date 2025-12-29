import React from "react";
import { Card } from "../Components/Ui/export.js";

function CookiePolicy() {
  return (
    <div className="max-w-5xl mx-auto px-4 py-10 text-text-primary">
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">Cookie Policy</h1>
        <p className="text-text-secondary">
          This policy explains how PyChat uses cookies and similar technologies.
        </p>
      </div>

      <div className="space-y-6">
        <Card title="1. What Are Cookies?">
          <p className="text-text-secondary">
            Cookies are small text files stored on your device when you visit a
            website. They help websites function properly, remember preferences,
            and improve user experience.
          </p>
        </Card>

        <Card title="2. How PyChat Uses Cookies">
          <p className="text-text-secondary mb-3">PyChat uses cookies to:</p>
          <ul className="list-disc list-inside space-y-1 text-text-secondary">
            <li>Maintain secure user sessions</li>
            <li>Remember user preferences and settings</li>
            <li>Improve performance and reliability</li>
            <li>Detect and prevent fraudulent activity</li>
          </ul>
        </Card>

        <Card title="3. Types of Cookies We Use">
          <ul className="list-disc list-inside space-y-2 text-text-secondary">
            <li>
              <strong>Essential Cookies:</strong> Required for core
              functionality such as authentication and security.
            </li>
            <li>
              <strong>Preference Cookies:</strong> Store user settings like
              theme or language preferences.
            </li>
            <li>
              <strong>Analytics Cookies:</strong> Help us understand how users
              interact with PyChat so we can improve features and performance.
            </li>
          </ul>
        </Card>

        <Card title="4. Third-Party Cookies">
          <p className="text-text-secondary">
            PyChat may use trusted third-party services for analytics or
            performance monitoring. These services may set their own cookies in
            accordance with their respective privacy policies.
          </p>
        </Card>

        <Card title="5. Managing Cookies">
          <p className="text-text-secondary">
            You can control or delete cookies through your browser settings.
            Please note that disabling essential cookies may affect the
            functionality of PyChat.
          </p>
        </Card>

        <Card title="6. Updates to This Policy">
          <p className="text-text-secondary">
            We may update this Cookie Policy from time to time. Any changes will
            be posted on this page, and continued use of PyChat indicates
            acceptance of the updated policy.
          </p>
        </Card>

        <Card title="7. Contact Us" footer="Last updated: August 2025">
          <p className="text-text-secondary">
            If you have questions about our use of cookies, please contact us at{" "}
            <span className="text-accent font-medium">support@pychat.app</span>.
          </p>
        </Card>
      </div>
    </div>
  );
}

export default CookiePolicy;
