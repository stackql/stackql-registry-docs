---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - vmmigration
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

Creates, updates, deletes, gets or lists a <code>sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The Source name. |
| <CopyableCode code="description" /> | `string` | User-provided description of the source. |
| <CopyableCode code="aws" /> | `object` | AwsSourceDetails message describes a specific source details for the AWS source type. |
| <CopyableCode code="azure" /> | `object` | AzureSourceDetails message describes a specific source details for the Azure source type. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time timestamp. |
| <CopyableCode code="encryption" /> | `object` | Encryption message describes the details of the applied encryption. |
| <CopyableCode code="labels" /> | `object` | The labels of the source. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time timestamp. |
| <CopyableCode code="vmware" /> | `object` | VmwareSourceDetails message describes a specific source details for the vmware source type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Gets details of a single Source. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Sources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Source in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Deletes a single Source. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Updates the parameters of a single Source. |

## `SELECT` examples

Lists Sources in a given project and location.

```sql
SELECT
name,
description,
aws,
azure,
createTime,
encryption,
labels,
updateTime,
vmware
FROM google.vmmigration.sources
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sources</code> resource.

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
INSERT INTO google.vmmigration.sources (
locationsId,
projectsId,
vmware,
aws,
azure,
labels,
description,
encryption
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ vmware }}',
'{{ aws }}',
'{{ azure }}',
'{{ labels }}',
'{{ description }}',
'{{ encryption }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: vmware
      value:
        - name: username
          value: string
        - name: password
          value: string
        - name: vcenterIp
          value: string
        - name: thumbprint
          value: string
        - name: resolvedVcenterHost
          value: string
    - name: aws
      value:
        - name: accessKeyCreds
          value:
            - name: accessKeyId
              value: string
            - name: secretAccessKey
              value: string
            - name: sessionToken
              value: string
        - name: awsRegion
          value: string
        - name: state
          value: string
        - name: error
          value:
            - name: code
              value: integer
            - name: message
              value: string
            - name: details
              value:
                - object
        - name: inventoryTagList
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: inventorySecurityGroupNames
          value:
            - string
        - name: migrationResourcesUserTags
          value: object
        - name: publicIp
          value: string
    - name: azure
      value:
        - name: clientSecretCreds
          value:
            - name: tenantId
              value: string
            - name: clientId
              value: string
            - name: clientSecret
              value: string
        - name: subscriptionId
          value: string
        - name: azureLocation
          value: string
        - name: state
          value: string
        - name: migrationResourcesUserTags
          value: object
        - name: resourceGroupId
          value: string
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: description
      value: string
    - name: encryption
      value:
        - name: kmsKey
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sources</code> resource.

```sql
/*+ update */
UPDATE google.vmmigration.sources
SET 
vmware = '{{ vmware }}',
aws = '{{ aws }}',
azure = '{{ azure }}',
labels = '{{ labels }}',
description = '{{ description }}',
encryption = '{{ encryption }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```

## `DELETE` example

Deletes the specified <code>sources</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.sources
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```
