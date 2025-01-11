---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - pcaconnectorscep
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>connector</code> resource or lists <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a Connector that allows certificate issuance through Simple Certificate Enrollment Protocol (SCEP)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorscep.connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_authority_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mobile_device_management" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="open_id_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-connector.html"><code>AWS::PCAConnectorSCEP::Connector</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="CertificateAuthorityArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>connectors</code> in a region.
```sql
SELECT
region,
certificate_authority_arn,
connector_arn,
type,
endpoint,
mobile_device_management,
open_id_configuration,
tags
FROM aws.pcaconnectorscep.connectors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>connector</code>.
```sql
SELECT
region,
certificate_authority_arn,
connector_arn,
type,
endpoint,
mobile_device_management,
open_id_configuration,
tags
FROM aws.pcaconnectorscep.connectors
WHERE region = 'us-east-1' AND data__Identifier = '<ConnectorArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.pcaconnectorscep.connectors (
 CertificateAuthorityArn,
 region
)
SELECT 
'{{ CertificateAuthorityArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcaconnectorscep.connectors (
 CertificateAuthorityArn,
 MobileDeviceManagement,
 Tags,
 region
)
SELECT 
 '{{ CertificateAuthorityArn }}',
 '{{ MobileDeviceManagement }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: connector
    props:
      - name: CertificateAuthorityArn
        value: '{{ CertificateAuthorityArn }}'
      - name: MobileDeviceManagement
        value: {}
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pcaconnectorscep.connectors
WHERE data__Identifier = '<ConnectorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connectors</code> resource, the following permissions are required:

### Create
```json
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificate,
acm-pca:GetCertificateAuthorityCertificate,
acm-pca:IssueCertificate,
pca-connector-scep:GetConnector,
pca-connector-scep:CreateConnector,
pca-connector-scep:TagResource
```

### Read
```json
pca-connector-scep:ListTagsForResource,
pca-connector-scep:GetConnector
```

### Delete
```json
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificate,
acm-pca:GetCertificateAuthorityCertificate,
acm-pca:IssueCertificate,
pca-connector-scep:GetConnector,
pca-connector-scep:DeleteConnector,
pca-connector-scep:UntagResource
```

### List
```json
pca-connector-scep:ListConnectors
```

### Update
```json
pca-connector-scep:ListTagsForResource,
pca-connector-scep:TagResource,
pca-connector-scep:UntagResource
```
