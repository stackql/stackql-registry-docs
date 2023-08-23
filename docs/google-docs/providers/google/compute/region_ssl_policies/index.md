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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_ssl_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_ssl_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `enabledFeatures` | `array` | [Output Only] The list of features enabled in the SSL policy. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a SslPolicy. An up-to-date fingerprint must be provided in order to update the SslPolicy, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an SslPolicy. |
| `warnings` | `array` | [Output Only] If potential misconfigurations are detected for this SSL policy, this field will be populated with warning messages. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `customFeatures` | `array` | A list of features enabled when the selected profile is CUSTOM. The method returns the set of features that can be specified in this list. This field must be empty if the profile is not CUSTOM. |
| `kind` | `string` | [Output only] Type of the resource. Always compute#sslPolicyfor SSL policies. |
| `region` | `string` | [Output Only] URL of the region where the regional SSL policy resides. This field is not applicable to global SSL policies. |
| `profile` | `string` | Profile specifies the set of SSL features that can be used by the load balancer when negotiating SSL with clients. This can be one of COMPATIBLE, MODERN, RESTRICTED, or CUSTOM. If using CUSTOM, the set of SSL features to enable must be specified in the customFeatures field. |
| `minTlsVersion` | `string` | The minimum version of SSL protocol that can be used by the clients to establish a connection with the load balancer. This can be one of TLS_1_0, TLS_1_1, TLS_1_2. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, region, sslPolicy` | Lists all of the ordered rules present in a single specified policy. |
| `list` | `SELECT` | `project, region` | Lists all the SSL policies that have been configured for the specified project and region. |
| `insert` | `INSERT` | `project, region` | Creates a new policy in the specified project and region using the data included in the request. |
| `delete` | `DELETE` | `project, region, sslPolicy` | Deletes the specified SSL policy. The SSL policy resource can be deleted only if it is not in use by any TargetHttpsProxy or TargetSslProxy resources. |
| `patch` | `EXEC` | `project, region, sslPolicy` | Patches the specified SSL policy with the data included in the request. |
