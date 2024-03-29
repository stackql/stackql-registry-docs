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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.managed_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the resource; defined by the server (output only) |
| `name` | `string` | User assigned name for this resource. Must be unique within the project. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes. |
| `description` | `string` | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the managed zone's function. |
| `kind` | `string` |  |
| `reverseLookupConfig` | `object` |  |
| `dnssecConfig` | `object` |  |
| `nameServers` | `array` | Delegate your managed_zone to these virtual name servers; defined by the server (output only) |
| `dnsName` | `string` | The DNS name of this managed zone, for instance "example.com.". |
| `labels` | `object` | User labels. |
| `cloudLoggingConfig` | `object` | Cloud Logging configurations for publicly visible zones. |
| `creationTime` | `string` | The time that this resource was created on the server. This is in RFC3339 text format. Output only. |
| `privateVisibilityConfig` | `object` |  |
| `peeringConfig` | `object` |  |
| `visibility` | `string` | The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources. |
| `nameServerSet` | `string` | Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users leave this field unset. If you need to use this field, contact your account team. |
| `serviceDirectoryConfig` | `object` | Contains information about Service Directory-backed zones. |
| `forwardingConfig` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managedZone, project` | Fetches the representation of an existing ManagedZone. |
| `list` | `SELECT` | `project` | Enumerates ManagedZones that have been created but not yet deleted. |
| `create` | `INSERT` | `project` | Creates a new ManagedZone. |
| `delete` | `DELETE` | `managedZone, project` | Deletes a previously created ManagedZone. |
| `_list` | `EXEC` | `project` | Enumerates ManagedZones that have been created but not yet deleted. |
| `patch` | `EXEC` | `managedZone, project` | Applies a partial update to an existing ManagedZone. |
| `update` | `EXEC` | `managedZone, project` | Updates an existing ManagedZone. |
