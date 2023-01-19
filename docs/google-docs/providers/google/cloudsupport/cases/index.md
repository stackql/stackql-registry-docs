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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsupport.cases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the case. |
| `description` | `string` | A broad description of the issue. |
| `testCase` | `boolean` | Whether this case was created for internal API testing and should not be acted on by the support team. |
| `updateTime` | `string` | Output only. The time this case was last updated. |
| `severity` | `string` | The severity of this case. Deprecated. Use priority instead. |
| `languageCode` | `string` | The language the user has requested to receive support in. This should be a BCP 47 language code (e.g., `"en"`, `"zh-CN"`, `"zh-TW"`, `"ja"`, `"ko"`). If no language or an unsupported language is specified, this field defaults to English (en). Language selection during case creation may affect your available support options. For a list of supported languages and their support working hours, see: https://cloud.google.com/support/docs/language-working-hours |
| `timeZone` | `string` | The timezone of the user who created the support case. It should be in a format IANA recognizes: https://www.iana.org/time-zones. There is no additional validation done by the API. |
| `creator` | `object` | An object containing information about the effective user and authenticated principal responsible for an action. |
| `displayName` | `string` | The short summary of the issue reported in this case. |
| `state` | `string` | Output only. The current status of the support case. |
| `escalated` | `boolean` | Whether the case is currently escalated. |
| `createTime` | `string` | Output only. The time this case was created. |
| `priority` | `string` | The priority of this case. If this is set, do not set severity. |
| `subscriberEmailAddresses` | `array` | The email addresses to receive updates on this case. |
| `classification` | `object` | A classification object with a product type and value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `parent` | Retrieve all cases under the specified parent. Note: Listing cases under an Organization returns only the cases directly parented by that organization. To retrieve all cases under an organization, including cases parented by projects under that organization, use `cases.search`. |
| `create` | `INSERT` | `parent` | Create a new case and associate it with the given Cloud resource. The case object must have the following fields set: display_name, description, classification, and severity. |
| `escalate` | `EXEC` | `name` | Escalate a case. Escalating a case will initiate the Cloud Support escalation management process. This operation is only available to certain Customer Care tiers. Go to https://cloud.google.com/support and look for 'Technical support escalations' in the feature list to find out which tiers are able to perform escalations. |
| `patch` | `EXEC` | `name` | Update the specified case. Only a subset of fields can be updated. |
| `search` | `EXEC` |  | Search cases using the specified query. |
