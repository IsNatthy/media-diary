# ReviewRoutes - Endpoints de comentarios (POST /api/library/:id/reviews, DELETE /api/reviews/:id)

from flask import Blueprint, jsonify, request, session
from server.src.services.review_service import ReviewService

review_bp = Blueprint('review', __name__)
review_service = ReviewService()

@review_bp.post('/')
def add_review():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    data = request.json
    # Ensure user_id is in data
    data['user_id'] = user_id
    
    review_service.add_review(data)
    return jsonify({"message": "Review added"}), 201

@review_bp.get('/content/<int:content_id>')
def get_reviews_for_content(content_id):
    reviews = review_service.get_reviews_for_content(content_id)
    return jsonify(reviews), 200

@review_bp.delete('/<int:review_id>')
def delete_review(review_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    success = review_service.delete_review(review_id, user_id)
    if success:
        return jsonify({"message": "Review deleted successfully"}), 200
    else:
        return jsonify({"message": "Review not found or unauthorized"}), 404