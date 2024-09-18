---
title: tls_inspection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - tls_inspection_policies
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>tls_inspection_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tls_inspection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.tls_inspection_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the resource. Name is of the form projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy} tls_inspection_policy should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="caPool" /> | `string` | Required. A CA pool resource used to issue interception certificates. The CA pool string has a relative resource path following the form "projects/{project}/locations/{location}/caPools/{ca_pool}". |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="customTlsFeatures" /> | `array` | Optional. List of custom TLS cipher suites selected. This field is valid only if the selected tls_feature_profile is CUSTOM. The compute.SslPoliciesService.ListAvailableFeatures method returns the set of features that can be specified in this list. Note that Secure Web Proxy does not yet honor this field. |
| <CopyableCode code="excludePublicCaSet" /> | `boolean` | Optional. If FALSE (the default), use our default set of public CAs in addition to any CAs specified in trust_config. These public CAs are currently based on the Mozilla Root Program and are subject to change over time. If TRUE, do not accept our default set of public CAs. Only CAs specified in trust_config will be accepted. This defaults to FALSE (use public CAs in addition to trust_config) for backwards compatibility, but trusting public root CAs is *not recommended* unless the traffic in question is outbound to public web servers. When possible, prefer setting this to "false" and explicitly specifying trusted CAs and certificates in a TrustConfig. Note that Secure Web Proxy does not yet honor this field. |
| <CopyableCode code="minTlsVersion" /> | `string` | Optional. Minimum TLS version that the firewall should use when negotiating connections with both clients and servers. If this is not set, then the default value is to allow the broadest set of clients and servers (TLS 1.0 or higher). Setting this to more restrictive values may improve security, but may also prevent the firewall from connecting to some clients or servers. Note that Secure Web Proxy does not yet honor this field. |
| <CopyableCode code="tlsFeatureProfile" /> | `string` | Optional. The selected Profile. If this is not set, then the default value is to allow the broadest set of clients and servers ("PROFILE_COMPATIBLE"). Setting this to more restrictive values may improve security, but may also prevent the TLS inspection proxy from connecting to some clients or servers. Note that Secure Web Proxy does not yet honor this field. |
| <CopyableCode code="trustConfig" /> | `string` | Optional. A TrustConfig resource used when making a connection to the TLS server. This is a relative resource path following the form "projects/{project}/locations/{location}/trustConfigs/{trust_config}". This is necessary to intercept TLS connections to servers with certificates signed by a private CA or self-signed certificates. Note that Secure Web Proxy does not yet honor this field. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_tls_inspection_policies_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tlsInspectionPoliciesId" /> | Gets details of a single TlsInspectionPolicy. |
| <CopyableCode code="projects_locations_tls_inspection_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TlsInspectionPolicies in a given project and location. |
| <CopyableCode code="projects_locations_tls_inspection_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new TlsInspectionPolicy in a given project and location. |
| <CopyableCode code="projects_locations_tls_inspection_policies_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, tlsInspectionPoliciesId" /> | Deletes a single TlsInspectionPolicy. |
| <CopyableCode code="projects_locations_tls_inspection_policies_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, tlsInspectionPoliciesId" /> | Updates the parameters of a single TlsInspectionPolicy. |

## `SELECT` examples

Lists TlsInspectionPolicies in a given project and location.

```sql
SELECT
name,
description,
caPool,
createTime,
customTlsFeatures,
excludePublicCaSet,
minTlsVersion,
tlsFeatureProfile,
trustConfig,
updateTime
FROM google.networksecurity.tls_inspection_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tls_inspection_policies</code> resource.

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
INSERT INTO google.networksecurity.tls_inspection_policies (
locationsId,
projectsId,
name,
description,
caPool,
trustConfig,
excludePublicCaSet,
minTlsVersion,
tlsFeatureProfile,
customTlsFeatures
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ caPool }}',
'{{ trustConfig }}',
true|false,
'{{ minTlsVersion }}',
'{{ tlsFeatureProfile }}',
'{{ customTlsFeatures }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
description: string
createTime: string
updateTime: string
caPool: string
trustConfig: string
excludePublicCaSet: boolean
minTlsVersion: string
tlsFeatureProfile: string
customTlsFeatures:
  - type: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tls_inspection_policies</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.tls_inspection_policies
SET 
name = '{{ name }}',
description = '{{ description }}',
caPool = '{{ caPool }}',
trustConfig = '{{ trustConfig }}',
excludePublicCaSet = true|false,
minTlsVersion = '{{ minTlsVersion }}',
tlsFeatureProfile = '{{ tlsFeatureProfile }}',
customTlsFeatures = '{{ customTlsFeatures }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tlsInspectionPoliciesId = '{{ tlsInspectionPoliciesId }}';
```

## `DELETE` example

Deletes the specified <code>tls_inspection_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.tls_inspection_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tlsInspectionPoliciesId = '{{ tlsInspectionPoliciesId }}';
```
