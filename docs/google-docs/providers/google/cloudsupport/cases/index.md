---
title: cases
hide_title: false
hide_table_of_contents: false
keywords:
  - cases
  - cloudsupport
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

Creates, updates, deletes, gets or lists a <code>cases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudsupport.cases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the case. |
| <CopyableCode code="description" /> | `string` | A broad description of the issue. |
| <CopyableCode code="classification" /> | `object` | A Case Classification represents the topic that a case is about. It's very important to use accurate classifications, because they're used to route your cases to specialists who can help you. A classification always has an ID that is its unique identifier. A valid ID is required when creating a case. |
| <CopyableCode code="contactEmail" /> | `string` | A user-supplied email address to send case update notifications for. This should only be used in BYOID flows, where we cannot infer the user's email address directly from their EUCs. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time this case was created. |
| <CopyableCode code="creator" /> | `object` | An Actor represents an entity that performed an action. For example, an actor could be a user who posted a comment on a support case, a user who uploaded an attachment, or a service account that created a support case. |
| <CopyableCode code="displayName" /> | `string` | The short summary of the issue reported in this case. |
| <CopyableCode code="escalated" /> | `boolean` | Whether the case is currently escalated. |
| <CopyableCode code="languageCode" /> | `string` | The language the user has requested to receive support in. This should be a BCP 47 language code (e.g., `"en"`, `"zh-CN"`, `"zh-TW"`, `"ja"`, `"ko"`). If no language or an unsupported language is specified, this field defaults to English (en). Language selection during case creation may affect your available support options. For a list of supported languages and their support working hours, see: https://cloud.google.com/support/docs/language-working-hours |
| <CopyableCode code="priority" /> | `string` | The priority of this case. |
| <CopyableCode code="state" /> | `string` | Output only. The current status of the support case. |
| <CopyableCode code="subscriberEmailAddresses" /> | `array` | The email addresses to receive updates on this case. |
| <CopyableCode code="testCase" /> | `boolean` | Whether this case was created for internal API testing and should not be acted on by the support team. |
| <CopyableCode code="timeZone" /> | `string` | The timezone of the user who created the support case. It should be in a format IANA recognizes: https://www.iana.org/time-zones. There is no additional validation done by the API. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time this case was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Retrieve a case. EXAMPLES: cURL: ```shell case="projects/some-project/cases/16033687" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().get( name="projects/some-project/cases/43595344", ) print(request.execute()) ``` |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Retrieve all cases under a parent, but not its children. For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`. EXAMPLES: cURL: ```shell parent="projects/some-project" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$parent/cases" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().list(parent="projects/some-project") print(request.execute()) ``` |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Create a new case and associate it with a parent. It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`. EXAMPLES: cURL: ```shell parent="projects/some-project" curl \ --request POST \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header 'Content-Type: application/json' \ --data '{ "display_name": "Test case created by me.", "description": "a random test case, feel free to close", "classification": { "id": "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8" }, "time_zone": "-07:00", "subscriber_email_addresses": [ "foo@domain.com", "bar@domain.com" ], "testCase": true, "priority": "P3" }' \ "https://cloudsupport.googleapis.com/v2/$parent/cases" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().create( parent="projects/some-project", body={ "displayName": "A Test Case", "description": "This is a test case.", "testCase": True, "priority": "P2", "classification": { "id": "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8" }, }, ) print(request.execute()) ``` |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="name" /> | Update a case. Only some fields can be updated. EXAMPLES: cURL: ```shell case="projects/some-project/cases/43595344" curl \ --request PATCH \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header "Content-Type: application/json" \ --data '{ "priority": "P1" }' \ "https://cloudsupport.googleapis.com/v2/$case?updateMask=priority" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().patch( name="projects/some-project/cases/43112854", body={ "displayName": "This is Now a New Title", "priority": "P2", }, ) print(request.execute()) ``` |
| <CopyableCode code="escalate" /> | `EXEC` | <CopyableCode code="name" /> | Escalate a case, starting the Google Cloud Support escalation management process. This operation is only available for some support services. Go to https://cloud.google.com/support and look for 'Technical support escalations' in the feature list to find out which ones let you do that. EXAMPLES: cURL: ```shell case="projects/some-project/cases/43595344" curl \ --request POST \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header "Content-Type: application/json" \ --data '{ "escalation": { "reason": "BUSINESS_IMPACT", "justification": "This is a test escalation." } }' \ "https://cloudsupport.googleapis.com/v2/$case:escalate" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().escalate( name="projects/some-project/cases/43595344", body={ "escalation": { "reason": "BUSINESS_IMPACT", "justification": "This is a test escalation.", }, }, ) print(request.execute()) ``` |

## `SELECT` examples

Retrieve a case. EXAMPLES: cURL: ```shell case="projects/some-project/cases/16033687" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = supportApiService.cases().get( name="projects/some-project/cases/43595344", ) print(request.execute()) ```

```sql
SELECT
name,
description,
classification,
contactEmail,
createTime,
creator,
displayName,
escalated,
languageCode,
priority,
state,
subscriberEmailAddresses,
testCase,
timeZone,
updateTime
FROM google.cloudsupport.cases
WHERE name = '{{ name }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cases</code> resource.

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
INSERT INTO google.cloudsupport.cases (
parent,
parentType,
languageCode,
classification,
contactEmail,
escalated,
description,
priority,
name,
testCase,
timeZone,
creator,
subscriberEmailAddresses,
displayName
)
SELECT 
'{{ parent }}',
'{{ parentType }}',
'{{ languageCode }}',
'{{ classification }}',
'{{ contactEmail }}',
true|false,
'{{ description }}',
'{{ priority }}',
'{{ name }}',
true|false,
'{{ timeZone }}',
'{{ creator }}',
'{{ subscriberEmailAddresses }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
languageCode: string
classification:
  id: string
  displayName: string
contactEmail: string
escalated: boolean
description: string
updateTime: string
priority: string
name: string
testCase: boolean
timeZone: string
state: string
createTime: string
creator:
  displayName: string
  email: string
  googleSupport: boolean
  username: string
subscriberEmailAddresses:
  - type: string
displayName: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cases</code> resource.

```sql
/*+ update */
UPDATE google.cloudsupport.cases
SET 
languageCode = '{{ languageCode }}',
classification = '{{ classification }}',
contactEmail = '{{ contactEmail }}',
escalated = true|false,
description = '{{ description }}',
priority = '{{ priority }}',
name = '{{ name }}',
testCase = true|false,
timeZone = '{{ timeZone }}',
creator = '{{ creator }}',
subscriberEmailAddresses = '{{ subscriberEmailAddresses }}',
displayName = '{{ displayName }}'
WHERE 
name = '{{ name }}';
```
