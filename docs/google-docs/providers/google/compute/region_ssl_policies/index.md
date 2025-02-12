---
title: region_ssl_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - region_ssl_policies
  - compute
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

Creates, updates, deletes, gets or lists a <code>region_ssl_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_ssl_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_ssl_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="customFeatures" /> | `array` | A list of features enabled when the selected profile is CUSTOM. The method returns the set of features that can be specified in this list. This field must be empty if the profile is not CUSTOM. |
| <CopyableCode code="enabledFeatures" /> | `array` | [Output Only] The list of features enabled in the SSL policy. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a SslPolicy. An up-to-date fingerprint must be provided in order to update the SslPolicy, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an SslPolicy. |
| <CopyableCode code="kind" /> | `string` | [Output only] Type of the resource. Always compute#sslPolicyfor SSL policies. |
| <CopyableCode code="minTlsVersion" /> | `string` | The minimum version of SSL protocol that can be used by the clients to establish a connection with the load balancer. This can be one of TLS_1_0, TLS_1_1, TLS_1_2. |
| <CopyableCode code="profile" /> | `string` | Profile specifies the set of SSL features that can be used by the load balancer when negotiating SSL with clients. This can be one of COMPATIBLE, MODERN, RESTRICTED, or CUSTOM. If using CUSTOM, the set of SSL features to enable must be specified in the customFeatures field. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional SSL policy resides. This field is not applicable to global SSL policies. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="warnings" /> | `array` | [Output Only] If potential misconfigurations are detected for this SSL policy, this field will be populated with warning messages. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, sslPolicy" /> | Lists all of the ordered rules present in a single specified policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Lists all the SSL policies that have been configured for the specified project and region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a new policy in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, sslPolicy" /> | Deletes the specified SSL policy. The SSL policy resource can be deleted only if it is not in use by any TargetHttpsProxy or TargetSslProxy resources. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, region, sslPolicy" /> | Patches the specified SSL policy with the data included in the request. |

## `SELECT` examples

Lists all the SSL policies that have been configured for the specified project and region.

```sql
SELECT
id,
name,
description,
creationTimestamp,
customFeatures,
enabledFeatures,
fingerprint,
kind,
minTlsVersion,
profile,
region,
selfLink,
warnings
FROM google.compute.region_ssl_policies
WHERE project = '{{ project }}'
AND region = '{{ region }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_ssl_policies</code> resource.

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
INSERT INTO google.compute.region_ssl_policies (
project,
region,
name,
description,
profile,
minTlsVersion,
enabledFeatures,
customFeatures,
fingerprint,
warnings,
region
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ profile }}',
'{{ minTlsVersion }}',
'{{ enabledFeatures }}',
'{{ customFeatures }}',
'{{ fingerprint }}',
'{{ warnings }}',
'{{ region }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: selfLink
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: profile
      value: string
    - name: minTlsVersion
      value: string
    - name: enabledFeatures
      value:
        - string
    - name: customFeatures
      value:
        - string
    - name: fingerprint
      value: string
    - name: warnings
      value:
        - - name: code
            value: string
          - name: message
            value: string
          - name: data
            value:
              - - name: key
                  value: string
                - name: value
                  value: string
    - name: region
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>region_ssl_policies</code> resource.

```sql
/*+ update */
UPDATE google.compute.region_ssl_policies
SET 
name = '{{ name }}',
description = '{{ description }}',
profile = '{{ profile }}',
minTlsVersion = '{{ minTlsVersion }}',
enabledFeatures = '{{ enabledFeatures }}',
customFeatures = '{{ customFeatures }}',
fingerprint = '{{ fingerprint }}',
warnings = '{{ warnings }}',
region = '{{ region }}'
WHERE 
project = '{{ project }}'
AND region = '{{ region }}'
AND sslPolicy = '{{ sslPolicy }}';
```

## `DELETE` example

Deletes the specified <code>region_ssl_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_ssl_policies
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND sslPolicy = '{{ sslPolicy }}';
```
