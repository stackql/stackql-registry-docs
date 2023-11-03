---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - opensearchservice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opensearchservice.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ClusterConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DomainName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AccessPolicies</code></td><td><code>object</code></td><td></td></tr><tr><td><code>EngineVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AdvancedOptions</code></td><td><code>object</code></td><td></td></tr><tr><td><code>LogPublishingOptions</code></td><td><code>object</code></td><td></td></tr><tr><td><code>SnapshotOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>VPCOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>NodeToNodeEncryptionOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DomainEndpointOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CognitoOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AdvancedSecurityOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DomainEndpoint</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DomainEndpoints</code></td><td><code>object</code></td><td></td></tr><tr><td><code>EBSOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DomainArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EncryptionAtRestOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this Domain.</td></tr><tr><td><code>ServiceSoftwareOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>OffPeakWindowOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SoftwareUpdateOptions</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.opensearchservice.domain
WHERE region = 'us-east-1' AND data__Identifier = '{DomainName}'
```
