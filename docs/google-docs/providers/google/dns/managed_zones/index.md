---
title: managed_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_zones
  - dns
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

Creates, updates, deletes, gets or lists a <code>managed_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.managed_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the resource; defined by the server (output only) |
| <CopyableCode code="name" /> | `string` | User assigned name for this resource. Must be unique within the project. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes. |
| <CopyableCode code="description" /> | `string` | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the managed zone's function. |
| <CopyableCode code="cloudLoggingConfig" /> | `object` | Cloud Logging configurations for publicly visible zones. |
| <CopyableCode code="creationTime" /> | `string` | The time that this resource was created on the server. This is in RFC3339 text format. Output only. |
| <CopyableCode code="dnsName" /> | `string` | The DNS name of this managed zone, for instance "example.com.". |
| <CopyableCode code="dnssecConfig" /> | `object` |  |
| <CopyableCode code="forwardingConfig" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="labels" /> | `object` | User labels. |
| <CopyableCode code="nameServerSet" /> | `string` | Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users leave this field unset. If you need to use this field, contact your account team. |
| <CopyableCode code="nameServers" /> | `array` | Delegate your managed_zone to these virtual name servers; defined by the server (output only) |
| <CopyableCode code="peeringConfig" /> | `object` |  |
| <CopyableCode code="privateVisibilityConfig" /> | `object` |  |
| <CopyableCode code="reverseLookupConfig" /> | `object` |  |
| <CopyableCode code="serviceDirectoryConfig" /> | `object` | Contains information about Service Directory-backed zones. |
| <CopyableCode code="visibility" /> | `string` | The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedZone, project" /> | Fetches the representation of an existing ManagedZone. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Enumerates ManagedZones that have been created but not yet deleted. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="project" /> | Creates a new ManagedZone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedZone, project" /> | Deletes a previously created ManagedZone. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="managedZone, project" /> | Applies a partial update to an existing ManagedZone. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="managedZone, project" /> | Updates an existing ManagedZone. |

## `SELECT` examples

Enumerates ManagedZones that have been created but not yet deleted.

```sql
SELECT
id,
name,
description,
cloudLoggingConfig,
creationTime,
dnsName,
dnssecConfig,
forwardingConfig,
kind,
labels,
nameServerSet,
nameServers,
peeringConfig,
privateVisibilityConfig,
reverseLookupConfig,
serviceDirectoryConfig,
visibility
FROM google.dns.managed_zones
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_zones</code> resource.

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
INSERT INTO google.dns.managed_zones (
project,
name,
dnsName,
description,
nameServers,
creationTime,
dnssecConfig,
nameServerSet,
visibility,
privateVisibilityConfig,
forwardingConfig,
labels,
peeringConfig,
reverseLookupConfig,
serviceDirectoryConfig,
cloudLoggingConfig
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ dnsName }}',
'{{ description }}',
'{{ nameServers }}',
'{{ creationTime }}',
'{{ dnssecConfig }}',
'{{ nameServerSet }}',
'{{ visibility }}',
'{{ privateVisibilityConfig }}',
'{{ forwardingConfig }}',
'{{ labels }}',
'{{ peeringConfig }}',
'{{ reverseLookupConfig }}',
'{{ serviceDirectoryConfig }}',
'{{ cloudLoggingConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: dnsName
      value: string
    - name: description
      value: string
    - name: id
      value: string
    - name: nameServers
      value:
        - string
    - name: creationTime
      value: string
    - name: dnssecConfig
      value:
        - name: state
          value: string
        - name: defaultKeySpecs
          value:
            - - name: keyType
                value: string
              - name: algorithm
                value: string
              - name: keyLength
                value: integer
              - name: kind
                value: string
        - name: nonExistence
          value: string
        - name: kind
          value: string
    - name: nameServerSet
      value: string
    - name: visibility
      value: string
    - name: privateVisibilityConfig
      value:
        - name: networks
          value:
            - - name: networkUrl
                value: string
              - name: kind
                value: string
        - name: gkeClusters
          value:
            - - name: gkeClusterName
                value: string
              - name: kind
                value: string
        - name: kind
          value: string
    - name: forwardingConfig
      value:
        - name: targetNameServers
          value:
            - - name: ipv4Address
                value: string
              - name: forwardingPath
                value: string
              - name: ipv6Address
                value: string
              - name: kind
                value: string
        - name: kind
          value: string
    - name: labels
      value: object
    - name: peeringConfig
      value:
        - name: targetNetwork
          value:
            - name: networkUrl
              value: string
            - name: deactivateTime
              value: string
            - name: kind
              value: string
        - name: kind
          value: string
    - name: reverseLookupConfig
      value:
        - name: kind
          value: string
    - name: serviceDirectoryConfig
      value:
        - name: namespace
          value:
            - name: namespaceUrl
              value: string
            - name: deletionTime
              value: string
            - name: kind
              value: string
        - name: kind
          value: string
    - name: cloudLoggingConfig
      value:
        - name: enableLogging
          value: boolean
        - name: kind
          value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_zones</code> resource.

```sql
/*+ update */
UPDATE google.dns.managed_zones
SET 
name = '{{ name }}',
dnsName = '{{ dnsName }}',
description = '{{ description }}',
nameServers = '{{ nameServers }}',
creationTime = '{{ creationTime }}',
dnssecConfig = '{{ dnssecConfig }}',
nameServerSet = '{{ nameServerSet }}',
visibility = '{{ visibility }}',
privateVisibilityConfig = '{{ privateVisibilityConfig }}',
forwardingConfig = '{{ forwardingConfig }}',
labels = '{{ labels }}',
peeringConfig = '{{ peeringConfig }}',
reverseLookupConfig = '{{ reverseLookupConfig }}',
serviceDirectoryConfig = '{{ serviceDirectoryConfig }}',
cloudLoggingConfig = '{{ cloudLoggingConfig }}'
WHERE 
managedZone = '{{ managedZone }}'
AND project = '{{ project }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>managed_zones</code> resource.

```sql
/*+ update */
REPLACE google.dns.managed_zones
SET 
name = '{{ name }}',
dnsName = '{{ dnsName }}',
description = '{{ description }}',
nameServers = '{{ nameServers }}',
creationTime = '{{ creationTime }}',
dnssecConfig = '{{ dnssecConfig }}',
nameServerSet = '{{ nameServerSet }}',
visibility = '{{ visibility }}',
privateVisibilityConfig = '{{ privateVisibilityConfig }}',
forwardingConfig = '{{ forwardingConfig }}',
labels = '{{ labels }}',
peeringConfig = '{{ peeringConfig }}',
reverseLookupConfig = '{{ reverseLookupConfig }}',
serviceDirectoryConfig = '{{ serviceDirectoryConfig }}',
cloudLoggingConfig = '{{ cloudLoggingConfig }}'
WHERE 
managedZone = '{{ managedZone }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>managed_zones</code> resource.

```sql
/*+ delete */
DELETE FROM google.dns.managed_zones
WHERE managedZone = '{{ managedZone }}'
AND project = '{{ project }}';
```
