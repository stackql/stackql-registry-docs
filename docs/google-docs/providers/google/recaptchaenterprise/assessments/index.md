
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

Creates, updates, deletes or gets an <code>assessment</code> resource or lists <code>assessments</code> in a region

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
fraudSignals,
fraudPreventionAssessment,
assessmentEnvironment,
privatePasswordLeakVerification,
accountDefenderAssessment,
firewallPolicyAssessment,
tokenProperties,
phoneFraudAssessment,
riskAnalysis,
name
)
SELECT 
'{{ projectsId }}',
'{{ accountVerification }}',
'{{ event }}',
'{{ fraudSignals }}',
'{{ fraudPreventionAssessment }}',
'{{ assessmentEnvironment }}',
'{{ privatePasswordLeakVerification }}',
'{{ accountDefenderAssessment }}',
'{{ firewallPolicyAssessment }}',
'{{ tokenProperties }}',
'{{ phoneFraudAssessment }}',
'{{ riskAnalysis }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: accountVerification
        value: '{{ accountVerification }}'
      - name: event
        value: '{{ event }}'
      - name: fraudSignals
        value: '{{ fraudSignals }}'
      - name: fraudPreventionAssessment
        value: '{{ fraudPreventionAssessment }}'
      - name: assessmentEnvironment
        value: '{{ assessmentEnvironment }}'
      - name: privatePasswordLeakVerification
        value: '{{ privatePasswordLeakVerification }}'
      - name: accountDefenderAssessment
        value: '{{ accountDefenderAssessment }}'
      - name: firewallPolicyAssessment
        value: '{{ firewallPolicyAssessment }}'
      - name: tokenProperties
        value: '{{ tokenProperties }}'
      - name: phoneFraudAssessment
        value: '{{ phoneFraudAssessment }}'
      - name: riskAnalysis
        value: '{{ riskAnalysis }}'
      - name: name
        value: '{{ name }}'

```
</TabItem>
</Tabs>
