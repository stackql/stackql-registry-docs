---
title: automations
hide_title: false
hide_table_of_contents: false
keywords:
  - automations
  - clouddeploy
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
<tr><td><b>Name</b></td><td><code>automations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="clouddeploy.automations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the `Automation`. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/deliveryPipelines/&#123;delivery_pipeline&#125;/automations/&#123;automation&#125;`. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the `Automation`. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints: * Annotations are key/value pairs. * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`). * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`). See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the automation was created. |
| <CopyableCode code="etag" /> | `string` | Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 63 characters. |
| <CopyableCode code="rules" /> | `array` | Required. List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution. |
| <CopyableCode code="selector" /> | `object` | AutomationResourceSelector contains the information to select the resources to which an Automation is going to be applied. |
| <CopyableCode code="serviceAccount" /> | `string` | Required. Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources. |
| <CopyableCode code="suspended" /> | `boolean` | Optional. When Suspended, automation is deactivated from execution. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `Automation`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time at which the automation was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationsId, deliveryPipelinesId, locationsId, projectsId" /> | Gets details of a single Automation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Lists Automations in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Creates a new Automation in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationsId, deliveryPipelinesId, locationsId, projectsId" /> | Deletes a single Automation resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="deliveryPipelinesId, locationsId, projectsId" /> | Lists Automations in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="automationsId, deliveryPipelinesId, locationsId, projectsId" /> | Updates the parameters of a single Automation resource. |
