---
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
  - recaptchaenterprise
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>assessments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.assessments" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an Assessment of the likelihood an event is legitimate. |
| <CopyableCode code="annotate" /> | `EXEC` | <CopyableCode code="assessmentsId, projectsId" /> | Annotates a previously created Assessment to provide additional information on whether the event turned out to be authentic or fraudulent. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assessments</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.recaptchaenterprise.assessments (
projectsId,
accountVerification,
event,
assessmentEnvironment,
privatePasswordLeakVerification
)
SELECT 
'{{ projectsId }}',
'{{ accountVerification }}',
'{{ event }}',
'{{ assessmentEnvironment }}',
'{{ privatePasswordLeakVerification }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
accountVerification:
  username: string
  languageCode: string
  endpoints:
    - phoneNumber: string
      emailAddress: string
      lastVerificationTime: string
      requestToken: string
  latestVerificationResult: string
event:
  ja3: string
  expectedAction: string
  hashedAccountId: string
  fraudPrevention: string
  wafTokenAssessment: boolean
  express: boolean
  firewallPolicyEvaluation: boolean
  userAgent: string
  transactionData:
    value: number
    currencyCode: string
    merchants:
      - emailVerified: boolean
        phoneNumber: string
        email: string
        creationMs: string
        accountId: string
        phoneVerified: boolean
    transactionId: string
    cardBin: string
    billingAddress:
      address:
        - type: string
      administrativeArea: string
      recipient: string
      postalCode: string
      locality: string
      regionCode: string
    user:
      emailVerified: boolean
      phoneNumber: string
      email: string
      creationMs: string
      accountId: string
      phoneVerified: boolean
    paymentMethod: string
    cardLastFour: string
    items:
      - name: string
        merchantAccountId: string
        quantity: string
        value: number
    shippingValue: number
    gatewayInfo:
      name: string
      cvvResponseCode: string
      avsResponseCode: string
      gatewayResponseCode: string
  userInfo:
    userIds:
      - email: string
        username: string
        phoneNumber: string
    accountId: string
    createAccountTime: string
  userIpAddress: string
  siteKey: string
  token: string
  headers:
    - type: string
  requestedUri: string
fraudSignals:
  cardSignals:
    cardLabels:
      - type: string
        enum: string
        enumDescriptions: string
  userSignals:
    activeDaysLowerBound: integer
    syntheticRisk: number
fraudPreventionAssessment:
  behavioralTrustVerdict:
    trust: number
  stolenInstrumentVerdict:
    risk: number
  transactionRisk: number
  cardTestingVerdict:
    risk: number
assessmentEnvironment:
  version: string
  client: string
privatePasswordLeakVerification:
  encryptedLeakMatchPrefixes:
    - type: string
      format: string
  lookupHashPrefix: string
  reencryptedUserCredentialsHash: string
  encryptedUserCredentialsHash: string
accountDefenderAssessment:
  labels:
    - type: string
      enumDescriptions: string
      enum: string
firewallPolicyAssessment:
  error:
    details:
      - additionalProperties: any
        type: string
    code: integer
    message: string
  firewallPolicy:
    name: string
    condition: string
    description: string
    actions:
      - redirect: {}
        allow: {}
        substitute:
          path: string
        includeRecaptchaScript: {}
        block: {}
        setHeader:
          value: string
          key: string
    path: string
tokenProperties:
  invalidReason: string
  hostname: string
  createTime: string
  valid: boolean
  iosBundleId: string
  androidPackageName: string
  action: string
phoneFraudAssessment:
  smsTollFraudVerdict:
    reasons:
      - type: string
        enumDescriptions: string
        enum: string
    risk: number
riskAnalysis:
  score: number
  extendedVerdictReasons:
    - type: string
  reasons:
    - type: string
      enum: string
      enumDescriptions: string
name: string

```
</TabItem>
</Tabs>
