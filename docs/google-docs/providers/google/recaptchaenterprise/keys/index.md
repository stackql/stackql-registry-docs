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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

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
wafSettings,
name,
iosSettings,
testingOptions,
webSettings,
androidSettings,
labels,
displayName,
expressSettings
)
SELECT 
'{{ projectsId }}',
'{{ wafSettings }}',
'{{ name }}',
'{{ iosSettings }}',
'{{ testingOptions }}',
'{{ webSettings }}',
'{{ androidSettings }}',
'{{ labels }}',
'{{ displayName }}',
'{{ expressSettings }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: wafSettings
      value:
        - name: wafFeature
          value: string
        - name: wafService
          value: string
    - name: name
      value: string
    - name: iosSettings
      value:
        - name: appleDeveloperId
          value:
            - name: keyId
              value: string
            - name: teamId
              value: string
            - name: privateKey
              value: string
        - name: allowedBundleIds
          value:
            - string
        - name: allowAllBundleIds
          value: boolean
    - name: createTime
      value: string
    - name: testingOptions
      value:
        - name: testingChallenge
          value: string
        - name: testingScore
          value: number
    - name: webSettings
      value:
        - name: challengeSecurityPreference
          value: string
        - name: allowedDomains
          value:
            - string
        - name: allowAllDomains
          value: boolean
        - name: allowAmpTraffic
          value: boolean
        - name: integrationType
          value: string
    - name: androidSettings
      value:
        - name: supportNonGoogleAppStoreDistribution
          value: boolean
        - name: allowedPackageNames
          value:
            - string
        - name: allowAllPackageNames
          value: boolean
    - name: labels
      value: object
    - name: displayName
      value: string
    - name: expressSettings
      value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>keys</code> resource.

```sql
/*+ update */
UPDATE google.recaptchaenterprise.keys
SET 
wafSettings = '{{ wafSettings }}',
name = '{{ name }}',
iosSettings = '{{ iosSettings }}',
testingOptions = '{{ testingOptions }}',
webSettings = '{{ webSettings }}',
androidSettings = '{{ androidSettings }}',
labels = '{{ labels }}',
displayName = '{{ displayName }}',
expressSettings = '{{ expressSettings }}'
WHERE 
keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.recaptchaenterprise.keys
WHERE keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}';
```
