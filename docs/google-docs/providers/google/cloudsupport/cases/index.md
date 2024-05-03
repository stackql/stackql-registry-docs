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
| <CopyableCode code="classification" /> | `object` | A classification object with a product type and value. |
| <CopyableCode code="contactEmail" /> | `string` | A user-supplied email address to send case update notifications for. This should only be used in BYOID flows, where we cannot infer the user's email address directly from their EUCs. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time this case was created. |
| <CopyableCode code="creator" /> | `object` | An object containing information about the effective user and authenticated principal responsible for an action. |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Retrieve the specified case. Here is an example of calling this endpoint using cURL: ```shell case="projects/some-project/cases/16033687" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case" ``` |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Create a new case and associate it with a Google Cloud Resource. The case object must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`. Here is an example of calling this endpoint using cURL: ```shell parent="projects/some-project" curl \ --request POST \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header 'Content-Type: application/json' \ --data '&#123; "display_name": "Test case created by me.", "description": "a random test case, feel free to close", "classification": &#123; "id": "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8" &#125;, "time_zone": "-07:00", "subscriber_email_addresses": [ "foo@domain.com", "bar@domain.com" ], "testCase": true, "priority": "P3" &#125;' \ "https://cloudsupport.googleapis.com/v2/$parent/cases" ``` |
| <CopyableCode code="escalate" /> | `EXEC` | <CopyableCode code="name" /> | Escalate a case. Escalating a case initiates the Google Cloud Support escalation management process. This operation is only available to certain Customer Care support services. Go to https://cloud.google.com/support and look for 'Technical support escalations' in the feature list to find out which support services let you perform escalations. Here is an example of calling this endpoint using cURL: ```shell case="projects/some-project/cases/43595344" curl \ --request POST \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header "Content-Type: application/json" \ --data '&#123; "escalation": &#123; "reason": "BUSINESS_IMPACT", "justification": "This is a test escalation." &#125; &#125;' \ "https://cloudsupport.googleapis.com/v2/$case:escalate" ``` |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="name" /> | Update the specified case. Only a subset of fields can be updated. Here is an example of calling this endpoint using cURL: ```shell case="projects/some-project/cases/43595344" curl \ --request PATCH \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header "Content-Type: application/json" \ --data '&#123; "priority": "P1" &#125;' \ "https://cloudsupport.googleapis.com/v2/$case?updateMask=priority" ``` |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | Search cases using the specified query. Here is an example of calling this endpoint using cURL: ```shell parent="projects/some-project" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$parent/cases:search" ``` |
