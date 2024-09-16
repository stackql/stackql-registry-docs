---
title: certificate_issuance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_issuance_configs
  - certificatemanager
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

Creates, updates, deletes, gets or lists a <code>certificate_issuance_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_issuance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.certificatemanager.certificate_issuance_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. A user-defined name of the certificate issuance config. CertificateIssuanceConfig names must be unique globally and match pattern `projects/*/locations/*/certificateIssuanceConfigs/*`. |
| <CopyableCode code="description" /> | `string` | Optional. One or more paragraphs of text description of a CertificateIssuanceConfig. |
| <CopyableCode code="certificateAuthorityConfig" /> | `object` | The CA that issues the workload certificate. It includes CA address, type, authentication to CA service, etc. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a CertificateIssuanceConfig. |
| <CopyableCode code="keyAlgorithm" /> | `string` | Required. The key algorithm to use when generating the private key. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with a CertificateIssuanceConfig. |
| <CopyableCode code="lifetime" /> | `string` | Required. Workload certificate lifetime requested. |
| <CopyableCode code="rotationWindowPercentage" /> | `integer` | Required. Specifies the percentage of elapsed time of the certificate lifetime to wait before renewing the certificate. Must be a number between 1-99, inclusive. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a CertificateIssuanceConfig. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateIssuanceConfigsId, locationsId, projectsId" /> | Gets details of a single CertificateIssuanceConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CertificateIssuanceConfigs in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new CertificateIssuanceConfig in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateIssuanceConfigsId, locationsId, projectsId" /> | Deletes a single CertificateIssuanceConfig. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="certificateIssuanceConfigsId, locationsId, projectsId" /> | Updates a CertificateIssuanceConfig. |

## `SELECT` examples

Lists CertificateIssuanceConfigs in a given project and location.

```sql
SELECT
name,
description,
certificateAuthorityConfig,
createTime,
keyAlgorithm,
labels,
lifetime,
rotationWindowPercentage,
updateTime
FROM google.certificatemanager.certificate_issuance_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_issuance_configs</code> resource.

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
INSERT INTO google.certificatemanager.certificate_issuance_configs (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
description,
certificateAuthorityConfig,
lifetime,
rotationWindowPercentage,
keyAlgorithm
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ certificateAuthorityConfig }}',
'{{ lifetime }}',
'{{ rotationWindowPercentage }}',
'{{ keyAlgorithm }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: description
      value: '{{ description }}'
    - name: certificateAuthorityConfig
      value: '{{ certificateAuthorityConfig }}'
    - name: lifetime
      value: '{{ lifetime }}'
    - name: rotationWindowPercentage
      value: '{{ rotationWindowPercentage }}'
    - name: keyAlgorithm
      value: '{{ keyAlgorithm }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificate_issuance_configs</code> resource.

```sql
/*+ update */
UPDATE google.certificatemanager.certificate_issuance_configs
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
certificateAuthorityConfig = '{{ certificateAuthorityConfig }}',
lifetime = '{{ lifetime }}',
rotationWindowPercentage = '{{ rotationWindowPercentage }}',
keyAlgorithm = '{{ keyAlgorithm }}'
WHERE 
certificateIssuanceConfigsId = '{{ certificateIssuanceConfigsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>certificate_issuance_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.certificatemanager.certificate_issuance_configs
WHERE certificateIssuanceConfigsId = '{{ certificateIssuanceConfigsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
