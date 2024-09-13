
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>automation</code> resource or lists <code>automations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.automations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the `Automation`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automations/{automation}`. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the `Automation`. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints: * Annotations are key/value pairs. * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`). * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`). See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the automation was created. |
| <CopyableCode code="etag" /> | `string` | Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 63 characters. |
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
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="automationsId, deliveryPipelinesId, locationsId, projectsId" /> | Updates the parameters of a single Automation resource. |

## `SELECT` examples

Lists Automations in a given project and location.

```sql
SELECT
name,
description,
annotations,
createTime,
etag,
labels,
rules,
selector,
serviceAccount,
suspended,
uid,
updateTime
FROM google.clouddeploy.automations
WHERE deliveryPipelinesId = '{{ deliveryPipelinesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>automations</code> resource.

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
INSERT INTO google.clouddeploy.automations (
deliveryPipelinesId,
locationsId,
projectsId,
name,
uid,
description,
createTime,
updateTime,
annotations,
labels,
etag,
suspended,
serviceAccount,
selector,
rules
)
SELECT 
'{{ deliveryPipelinesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ uid }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ annotations }}',
'{{ labels }}',
'{{ etag }}',
true|false,
'{{ serviceAccount }}',
'{{ selector }}',
'{{ rules }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: uid
        value: '{{ uid }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: labels
        value: '{{ labels }}'
      - name: etag
        value: '{{ etag }}'
      - name: suspended
        value: '{{ suspended }}'
      - name: serviceAccount
        value: '{{ serviceAccount }}'
      - name: selector
        value: '{{ selector }}'
      - name: rules
        value: '{{ rules }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a automation only if the necessary resources are available.

```sql
UPDATE google.clouddeploy.automations
SET 
name = '{{ name }}',
uid = '{{ uid }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
annotations = '{{ annotations }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
suspended = true|false,
serviceAccount = '{{ serviceAccount }}',
selector = '{{ selector }}',
rules = '{{ rules }}'
WHERE 
automationsId = '{{ automationsId }}'
AND deliveryPipelinesId = '{{ deliveryPipelinesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified automation resource.

```sql
DELETE FROM google.clouddeploy.automations
WHERE automationsId = '{{ automationsId }}'
AND deliveryPipelinesId = '{{ deliveryPipelinesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
