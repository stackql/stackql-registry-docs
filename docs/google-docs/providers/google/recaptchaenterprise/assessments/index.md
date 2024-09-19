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
assessmentEnvironment,
accountVerification,
event,
privatePasswordLeakVerification
)
SELECT 
'{{ projectsId }}',
'{{ assessmentEnvironment }}',
'{{ accountVerification }}',
'{{ event }}',
'{{ privatePasswordLeakVerification }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: phoneFraudAssessment
      value:
        - name: smsTollFraudVerdict
          value:
            - name: reasons
              value:
                - string
            - name: risk
              value: number
    - name: name
      value: string
    - name: assessmentEnvironment
      value:
        - name: version
          value: string
        - name: client
          value: string
    - name: accountVerification
      value:
        - name: latestVerificationResult
          value: string
        - name: languageCode
          value: string
        - name: endpoints
          value:
            - - name: emailAddress
                value: string
              - name: requestToken
                value: string
              - name: phoneNumber
                value: string
              - name: lastVerificationTime
                value: string
        - name: username
          value: string
    - name: tokenProperties
      value:
        - name: hostname
          value: string
        - name: valid
          value: boolean
        - name: invalidReason
          value: string
        - name: androidPackageName
          value: string
        - name: createTime
          value: string
        - name: action
          value: string
        - name: iosBundleId
          value: string
    - name: event
      value:
        - name: userIpAddress
          value: string
        - name: fraudPrevention
          value: string
        - name: wafTokenAssessment
          value: boolean
        - name: requestedUri
          value: string
        - name: userAgent
          value: string
        - name: expectedAction
          value: string
        - name: token
          value: string
        - name: hashedAccountId
          value: string
        - name: firewallPolicyEvaluation
          value: boolean
        - name: express
          value: boolean
        - name: headers
          value:
            - string
        - name: ja3
          value: string
        - name: siteKey
          value: string
        - name: transactionData
          value:
            - name: billingAddress
              value:
                - name: recipient
                  value: string
                - name: address
                  value:
                    - string
                - name: postalCode
                  value: string
                - name: regionCode
                  value: string
                - name: administrativeArea
                  value: string
                - name: locality
                  value: string
            - name: user
              value:
                - name: phoneNumber
                  value: string
                - name: emailVerified
                  value: boolean
                - name: email
                  value: string
                - name: accountId
                  value: string
                - name: creationMs
                  value: string
                - name: phoneVerified
                  value: boolean
            - name: paymentMethod
              value: string
            - name: cardBin
              value: string
            - name: items
              value:
                - - name: value
                    value: number
                  - name: quantity
                    value: string
                  - name: merchantAccountId
                    value: string
                  - name: name
                    value: string
            - name: currencyCode
              value: string
            - name: gatewayInfo
              value:
                - name: avsResponseCode
                  value: string
                - name: name
                  value: string
                - name: gatewayResponseCode
                  value: string
                - name: cvvResponseCode
                  value: string
            - name: transactionId
              value: string
            - name: shippingValue
              value: number
            - name: cardLastFour
              value: string
            - name: value
              value: number
            - name: merchants
              value:
                - - name: phoneNumber
                    value: string
                  - name: emailVerified
                    value: boolean
                  - name: email
                    value: string
                  - name: accountId
                    value: string
                  - name: creationMs
                    value: string
                  - name: phoneVerified
                    value: boolean
        - name: userInfo
          value:
            - name: userIds
              value:
                - - name: email
                    value: string
                  - name: username
                    value: string
                  - name: phoneNumber
                    value: string
            - name: createAccountTime
              value: string
            - name: accountId
              value: string
    - name: firewallPolicyAssessment
      value:
        - name: error
          value:
            - name: message
              value: string
            - name: code
              value: integer
            - name: details
              value:
                - object
        - name: firewallPolicy
          value:
            - name: description
              value: string
            - name: actions
              value:
                - - name: allow
                    value: []
                  - name: substitute
                    value:
                      - name: path
                        value: string
                  - name: setHeader
                    value:
                      - name: value
                        value: string
                      - name: key
                        value: string
                  - name: includeRecaptchaScript
                    value: []
                  - name: block
                    value: []
                  - name: redirect
                    value: []
            - name: path
              value: string
            - name: condition
              value: string
            - name: name
              value: string
    - name: privatePasswordLeakVerification
      value:
        - name: encryptedLeakMatchPrefixes
          value:
            - string
        - name: reencryptedUserCredentialsHash
          value: string
        - name: lookupHashPrefix
          value: string
        - name: encryptedUserCredentialsHash
          value: string
    - name: fraudSignals
      value:
        - name: cardSignals
          value:
            - name: cardLabels
              value:
                - string
        - name: userSignals
          value:
            - name: activeDaysLowerBound
              value: integer
            - name: syntheticRisk
              value: number
    - name: riskAnalysis
      value:
        - name: reasons
          value:
            - string
        - name: extendedVerdictReasons
          value:
            - string
        - name: score
          value: number
    - name: accountDefenderAssessment
      value:
        - name: labels
          value:
            - string
    - name: fraudPreventionAssessment
      value:
        - name: stolenInstrumentVerdict
          value:
            - name: risk
              value: number
        - name: transactionRisk
          value: number
        - name: cardTestingVerdict
          value:
            - name: risk
              value: number
        - name: behavioralTrustVerdict
          value:
            - name: trust
              value: number

```
</TabItem>
</Tabs>
