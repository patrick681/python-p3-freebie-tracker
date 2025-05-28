from flask import request, jsonify, abort
from lib.models import db, Company, Dev, Freebie

# --- Helper functions ---
def get_company_or_404(company_id):
    company = Company.query.get(company_id)
    if not company:
        abort(404, description=f"Company with id {company_id} not found")
    return company

def get_dev_or_404(dev_id):
    dev = Dev.query.get(dev_id)
    if not dev:
        abort(404, description=f"Dev with id {dev_id} not found")
    return dev

def get_freebie_or_404(freebie_id):
    freebie = Freebie.query.get(freebie_id)
    if not freebie:
        abort(404, description=f"Freebie with id {freebie_id} not found")
    return freebie


def register_routes(app):

    # --- Routes for Companies ---

    @app.route('/companies', methods=['GET'])
    def get_companies():
        companies = Company.query.all()
        return jsonify([c.to_dict() for c in companies])

    @app.route('/companies/<int:id>', methods=['GET'])
    def get_company(id):
        company = get_company_or_404(id)
        return jsonify(company.to_dict())

    @app.route('/companies', methods=['POST'])
    def create_company():
        data = request.get_json()
        new_company = Company(name=data['name'], founding_year=data['founding_year'])
        db.session.add(new_company)
        db.session.commit()
        return jsonify(new_company.to_dict()), 201

    @app.route('/companies/<int:id>', methods=['PUT'])
    def update_company(id):
        company = get_company_or_404(id)
        data = request.get_json()
        company.name = data.get('name', company.name)
        company.founding_year = data.get('founding_year', company.founding_year)
        db.session.commit()
        return jsonify(company.to_dict())

    @app.route('/companies/<int:id>', methods=['DELETE'])
    def delete_company(id):
        company = get_company_or_404(id)
        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': 'Company deleted'}), 204

    # --- Routes for Devs ---

    @app.route('/devs', methods=['GET'])
    def get_devs():
        devs = Dev.query.all()
        return jsonify([d.to_dict() for d in devs])

    @app.route('/devs/<int:id>', methods=['GET'])
    def get_dev(id):
        dev = get_dev_or_404(id)
        return jsonify(dev.to_dict())

    @app.route('/devs', methods=['POST'])
    def create_dev():
        data = request.get_json()
        new_dev = Dev(name=data['name'])
        db.session.add(new_dev)
        db.session.commit()
        return jsonify(new_dev.to_dict()), 201

    @app.route('/devs/<int:id>', methods=['PUT'])
    def update_dev(id):
        dev = get_dev_or_404(id)
        data = request.get_json()
        dev.name = data.get('name', dev.name)
        db.session.commit()
        return jsonify(dev.to_dict())

    @app.route('/devs/<int:id>', methods=['DELETE'])
    def delete_dev(id):
        dev = get_dev_or_404(id)
        db.session.delete(dev)
        db.session.commit()
        return jsonify({'message': 'Dev deleted'}), 204

    # --- Routes for Freebies ---

    @app.route('/freebies', methods=['GET'])
    def get_freebies():
        freebies = Freebie.query.all()
        return jsonify([f.to_dict() for f in freebies])

    @app.route('/freebies/<int:id>', methods=['GET'])
    def get_freebie(id):
        freebie = get_freebie_or_404(id)
        return jsonify(freebie.to_dict())

    @app.route('/freebies', methods=['POST'])
    def create_freebie():
        data = request.get_json()
        new_freebie = Freebie(
            item_name=data['item_name'],
            value=data['value'],
            company_id=data['company_id'],
            dev_id=data['dev_id']
        )
        db.session.add(new_freebie)
        db.session.commit()
        return jsonify(new_freebie.to_dict()), 201

    @app.route('/freebies/<int:id>', methods=['PUT'])
    def update_freebie(id):
        freebie = get_freebie_or_404(id)
        data = request.get_json()
        freebie.item_name = data.get('item_name', freebie.item_name)
        freebie.value = data.get('value', freebie.value)
        freebie.company_id = data.get('company_id', freebie.company_id)
        freebie.dev_id = data.get('dev_id', freebie.dev_id)
        db.session.commit()
        return jsonify(freebie.to_dict())

    @app.route('/freebies/<int:id>', methods=['DELETE'])
    def delete_freebie(id):
        freebie = get_freebie_or_404(id)
        db.session.delete(freebie)
        db.session.commit()
        return jsonify({'message': 'Freebie deleted'}), 204

    # --- Bonus: Get all freebies a dev owns ---
    @app.route('/devs/<int:dev_id>/freebies', methods=['GET'])
    def freebies_by_dev(dev_id):
        dev = get_dev_or_404(dev_id)
        return jsonify([f.to_dict() for f in dev.freebies])
