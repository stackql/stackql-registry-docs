
---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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

Creates, updates, deletes or gets an <code>key</code> resource or lists <code>keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name for the Key in the format `projects/{project}/keys/{key}`. |
| <CopyableCode code="androidSettings" /> | `object` | Settings specific to keys that can be used by Android apps. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp corresponding to the creation of this key. |
| <CopyableCode code="displayName" /> | `string` | Required. Human-readable display name of this key. Modifiable by user. |
| <CopyableCode code="expressSettings" /> | `object` | Settings specific to keys that can be used for reCAPTCHA Express. |
| <CopyableCode code="iosSettings" /> | `object` | Settings specific to keys that can be used by iOS apps. |
| <CopyableCode code="labels" /> | `object` | Optional. See [Creating and managing labels] (https://cloud.google.com/recaptcha/docs/labels). |
| <CopyableCode code="testingOptions" /> | `object` | Options for user acceptance testing. |
| <CopyableCode code="wafSettings" /> | `object` | Settings specific to keys that can be used for WAF (Web Application Firewall). |
| <CopyableCode code="webSettings" /> | `object` | Settings specific to keys that can be used by websites. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keysId, projectsId" /> | Returns the specified key. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns the list of all keys that belong to a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new reCAPTCHA Enterprise key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keysId, projectsId" /> | Deletes the specified key. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="keysId, projectsId" /> | Updates the specified key. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="keysId, projectsId" /> | Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise. Once a key is migrated, it can be used from either product. SiteVerify requests are billed as CreateAssessment calls. You must be authenticated as one of the current owners of the reCAPTCHA Key, and your user must have the reCAPTCHA Enterprise Admin IAM role in the destination project. |

## `SELECT` examples

Returns the list of all keys that belong to a project.

```sql
SELECT
name,
androidSettings,
createTime,
displayName,
expressSettings,
iosSettings,
labels,
testingOptions,
wafSettings,
webSettings
FROM google.recaptchaenterprise.keys
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keys</code> resource.

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
INSERT INTO google.recaptchaenterprise.keys (
projectsId,
displayName,
name,
webSettings,
wafSettings,
testingOptions,
labels,
androidSettings,
expressSettings,
iosSettings,
createTime
)
SELECT 
'{{ projectsId }}',
'{{ displayName }}',
'{{ name }}',
'{{ webSettings }}',
'{{ wafSettings }}',
'{{ testingOptions }}',
'{{ labels }}',
'{{ androidSettings }}',
'{{ expressSettings }}',
'{{ iosSettings }}',
'{{ createTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: displayName
        value: '{{ displayName }}'
      - name: name
        value: '{{ name }}'
      - name: webSettings
        value: '{{ webSettings }}'
      - name: wafSettings
        value: '{{ wafSettings }}'
      - name: testingOptions
        value: '{{ testingOptions }}'
      - name: labels
        value: '{{ labels }}'
      - name: androidSettings
        value: '{{ androidSettings }}'
      - name: expressSettings
        value: '{{ expressSettings }}'
      - name: iosSettings
        value: '{{ iosSettings }}'
      - name: createTime
        value: '{{ createTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a key only if the necessary resources are available.

```sql
UPDATE google.recaptchaenterprise.keys
SET 
displayName = '{{ displayName }}',
name = '{{ name }}',
webSettings = '{{ webSettings }}',
wafSettings = '{{ wafSettings }}',
testingOptions = '{{ testingOptions }}',
labels = '{{ labels }}',
androidSettings = '{{ androidSettings }}',
expressSettings = '{{ expressSettings }}',
iosSettings = '{{ iosSettings }}',
createTime = '{{ createTime }}'
WHERE 
keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified key resource.

```sql
DELETE FROM google.recaptchaenterprise.keys
WHERE keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}';
```
